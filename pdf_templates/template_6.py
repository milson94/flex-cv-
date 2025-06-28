import io
import os
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, FrameBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# --- Color Palette matching Ellen Johnson template ---
COLOR_TEXT_MAIN = HexColor('#333333')
COLOR_TEXT_MUTED = HexColor('#666666')
COLOR_TEXT_HEADER = HexColor('#1a365d')  # Dark blue
COLOR_ACCENT_BLUE = HexColor('#3182ce')  # Blue accent
COLOR_SECTION_BLUE = HexColor('#2b6cb0')  # Blue for section titles
COLOR_BACKGROUND_LIGHT = HexColor('#f7fafc')

class PhotoResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        self.profile_image_path = kwargs.pop('profile_image_path', None)
        self.full_name = kwargs.pop('full_name', '')
        BaseDocTemplate.__init__(self, filename, **kwargs)

        # Single page layout with photo in top-right
        frame_main = Frame(self.leftMargin, self.bottomMargin,
                           self.width, self.height, id='main_content', showBoundary=0,
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        
        main_page = PageTemplate(id='MainPage', frames=[frame_main], 
                                onPage=self.draw_page_elements)
        self.addPageTemplates([main_page])

    def draw_page_elements(self, canvas, doc):
        """Draw the profile image and any background elements"""
        canvas.saveState()
        
        # Profile Image (Top Right corner)
        if self.profile_image_path and os.path.exists(self.profile_image_path):
            try:
                # Image dimensions and position
                img_size = 1.4 * inch
                margin_from_edge = 0.2 * inch
                
                # Calculate position from top-right corner
                img_x = doc.pagesize[0] - doc.rightMargin - img_size - margin_from_edge
                img_y = doc.pagesize[1] - doc.topMargin - img_size - margin_from_edge
                
                # Create circular clipping path
                center_x = img_x + img_size/2
                center_y = img_y + img_size/2
                radius = img_size/2
                
                # Draw circular background
                canvas.setFillColor(HexColor('#e2e8f0'))
                canvas.circle(center_x, center_y, radius + 3, stroke=0, fill=1)
                
                # Create clipping path for circular image
                path = canvas.beginPath()
                path.circle(center_x, center_y, radius)
                canvas.clipPath(path, stroke=0, fill=0)
                
                # Draw the image
                canvas.drawImage(self.profile_image_path, img_x, img_y, 
                               width=img_size, height=img_size, mask='auto')
                
                print(f"Successfully drew profile image at ({img_x}, {img_y})")
                
            except Exception as e:
                print(f"Error drawing profile image: {e}")
                # Draw a placeholder circle
                canvas.setFillColor(HexColor('#cbd5e0'))
                canvas.circle(center_x, center_y, radius, stroke=1, fill=1)
                canvas.setFillColor(HexColor('#4a5568'))
                canvas.setFont('Helvetica', 12)
                canvas.drawCentredText(center_x, center_y, "Photo")
        
        canvas.restoreState()


def generate_pdf(data):
    buffer = io.BytesIO()
    
    # Get profile image path from data
    profile_image_path = data.get('profile_image_path')
    
    # Debug: Print image path info
    print(f"Profile image path: {profile_image_path}")
    if profile_image_path:
        print(f"Image exists: {os.path.exists(profile_image_path)}")
    
    doc = PhotoResumeDocTemplate(buffer, pagesize=letter,
                                leftMargin=0.75*inch, rightMargin=0.75*inch,
                                topMargin=0.75*inch, bottomMargin=0.75*inch,
                                profile_image_path=profile_image_path,
                                full_name=data.get('full_name', ''))

    styles = getSampleStyleSheet()
    
    # --- Define Styles matching Ellen Johnson template ---
    styles.add(ParagraphStyle(name='FullName', fontName='Helvetica-Bold', fontSize=32, 
                              textColor=COLOR_TEXT_HEADER, spaceBefore=0, leading=36, 
                              alignment=TA_LEFT, spaceAfter=0.1*inch))
    styles.add(ParagraphStyle(name='JobTitleHeader', fontName='Helvetica', fontSize=14, 
                              textColor=COLOR_ACCENT_BLUE, spaceAfter=0.1*inch, leading=16))
    styles.add(ParagraphStyle(name='ContactInfo', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MUTED, leading=12, spaceAfter=0.2*inch))

    # Section styles
    styles.add(ParagraphStyle(name='SectionTitle', fontName='Helvetica-Bold', fontSize=12, 
                              textColor=COLOR_SECTION_BLUE, spaceBefore=0.25*inch, spaceAfter=0.1*inch, 
                              leading=14, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='BodyText', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=13, spaceAfter=0.05*inch, alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='JobTitle', fontName='Helvetica-Bold', fontSize=11, 
                              textColor=COLOR_TEXT_MAIN, leading=14, spaceAfter=0.02*inch))
    styles.add(ParagraphStyle(name='CompanyDate', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MUTED, leading=12, spaceAfter=0.05*inch))
    styles.add(ParagraphStyle(name='BulletPoint', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=12, leftIndent=15, 
                              firstLineIndent=0, spaceBefore=1, bulletIndent=5))
    styles.add(ParagraphStyle(name='AchievementTitle', fontName='Helvetica-Bold', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=13, spaceAfter=0.02*inch))
    styles.add(ParagraphStyle(name='AchievementDesc', fontName='Helvetica', fontSize=9, 
                              textColor=COLOR_TEXT_MUTED, leading=11, spaceAfter=0.1*inch))

    # --- Build the story ---
    story = []
    
    # Header section with space for photo
    header_table_data = []
    
    # Left side: Name, title, contact info
    header_left_content = []
    if data.get('full_name'):
        header_left_content.append(Paragraph(data['full_name'].upper(), styles['FullName']))
    if data.get('title_subtitle'):
        header_left_content.append(Paragraph(data['title_subtitle'], styles['JobTitleHeader']))
    
    # Contact information
    contact_items = []
    if data.get('email'): contact_items.append(f"📧 {data['email']}")
    if data.get('linkedin'): contact_items.append(f"🔗 {data['linkedin']}")
    if data.get('location'): contact_items.append(f"📍 {data['location']}")
    if contact_items:
        header_left_content.append(Paragraph("  ".join(contact_items), styles['ContactInfo']))
    
    # Right side: Space for photo (handled by canvas drawing)
    header_right_content = [Spacer(1, 1.6*inch)]  # Space for photo
    
    # Create header table
    header_table_data.append([header_left_content, header_right_content])
    header_table = Table(header_table_data, colWidths=[4.5*inch, 2.5*inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 0.2*inch))

    # Get section order from data
    section_order = data.get('section_order', ['summary', 'experience', 'education', 'achievements', 'courses', 'skills', 'languages'])

    # Process sections in order
    for section_key in section_order:
        if section_key == 'summary':
            if data.get('summary'):
                story.append(Paragraph('SUMMARY', styles['SectionTitle']))
                story.append(Paragraph(data['summary'], styles['BodyText']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'experience':
            experiences = data.get('experiences', [])
            if experiences:
                story.append(Paragraph('EXPERIENCE', styles['SectionTitle']))
                for exp in experiences:
                    if exp.get('title'):
                        story.append(Paragraph(exp['title'], styles['JobTitle']))
                    
                    # Company, location, and dates
                    company_parts = []
                    if exp.get('company'):
                        company_parts.append(exp['company'])
                    if exp.get('location'):
                        company_parts.append(exp['location'])
                    
                    # Format dates
                    if exp.get('start_date'):
                        date_str = exp['start_date']
                        if exp.get('end_date'):
                            date_str += f" - {exp['end_date']}"
                        elif exp.get('is_present'):
                            date_str += " - Present"
                        company_parts.append(date_str)
                    
                    if company_parts:
                        story.append(Paragraph(" | ".join(company_parts), styles['CompanyDate']))
                    
                    # Description with bullet points
                    if exp.get('description'):
                        desc_lines = exp['description'].split('\n')
                        for line in desc_lines:
                            line = line.strip()
                            if line.startswith(('-', '*', '•')):
                                story.append(Paragraph(f"• {line[1:].strip()}", styles['BulletPoint']))
                            elif line:
                                story.append(Paragraph(line, styles['BodyText']))
                    
                    story.append(Spacer(1, 0.15*inch))

        elif section_key == 'education':
            education_entries = data.get('education_entries', [])
            if education_entries:
                story.append(Paragraph('EDUCATION', styles['SectionTitle']))
                for edu in education_entries:
                    if edu.get('degree'):
                        story.append(Paragraph(edu['degree'], styles['JobTitle']))
                    
                    # Institution, location, and dates
                    edu_parts = []
                    if edu.get('institution'):
                        edu_parts.append(edu['institution'])
                    if edu.get('edu_location'):
                        edu_parts.append(edu['edu_location'])
                    
                    if edu.get('start_date'):
                        date_str = edu['start_date']
                        if edu.get('end_date'):
                            date_str += f" - {edu['end_date']}"
                        elif edu.get('is_present'):
                            date_str += " - Present"
                        edu_parts.append(date_str)
                    
                    if edu_parts:
                        story.append(Paragraph(" | ".join(edu_parts), styles['CompanyDate']))
                    
                    if edu.get('edu_details'):
                        story.append(Paragraph(edu['edu_details'], styles['BodyText']))
                    
                    story.append(Spacer(1, 0.1*inch))

        elif section_key == 'achievements':
            key_achievements = data.get('key_achievements', [])
            if key_achievements:
                story.append(Paragraph('KEY ACHIEVEMENTS', styles['SectionTitle']))
                for ach in key_achievements:
                    if ach.get('title'):
                        story.append(Paragraph(f"🏆 {ach['title']}", styles['AchievementTitle']))
                        if ach.get('description'):
                            story.append(Paragraph(ach['description'], styles['AchievementDesc']))

        elif section_key == 'courses':
            courses = data.get('courses', [])
            if courses:
                story.append(Paragraph('CERTIFICATION', styles['SectionTitle']))
                for course in courses:
                    if course.get('title'):
                        story.append(Paragraph(course['title'], styles['AchievementTitle']))
                        if course.get('description'):
                            story.append(Paragraph(course['description'], styles['AchievementDesc']))

        elif section_key == 'skills':
            if data.get('skills'):
                story.append(Paragraph('SKILLS', styles['SectionTitle']))
                skills_list = [skill.strip() for skill in data['skills'].split(',')]
                
                # Create a skills table for better layout
                skills_table_data = []
                row = []
                for i, skill in enumerate(skills_list):
                    if skill:
                        row.append(skill)
                        if len(row) == 4 or i == len(skills_list) - 1:  # 4 skills per row
                            while len(row) < 4:
                                row.append('')  # Pad row
                            skills_table_data.append(row)
                            row = []
                
                if skills_table_data:
                    skills_table = Table(skills_table_data)
                    skills_table.setStyle(TableStyle([
                        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
                        ('FONTSIZE', (0,0), (-1,-1), 9),
                        ('TEXTCOLOR', (0,0), (-1,-1), COLOR_TEXT_MAIN),
                        ('VALIGN', (0,0), (-1,-1), 'TOP'),
                        ('LEFTPADDING', (0,0), (-1,-1), 8),
                        ('RIGHTPADDING', (0,0), (-1,-1), 8),
                        ('TOPPADDING', (0,0), (-1,-1), 4),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                        ('BACKGROUND', (0,0), (-1,-1), HexColor('#f8f9fa')),
                        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#e9ecef')),
                    ]))
                    story.append(skills_table)
                    story.append(Spacer(1, 0.1*inch))

        elif section_key == 'languages':
            languages = data.get('languages', [])
            if languages:
                story.append(Paragraph('LANGUAGES', styles['SectionTitle']))
                for lang in languages:
                    if lang.get('name'):
                        level_info = []
                        if lang.get('level'):
                            level_info.append(f"Overall: {lang['level']}")
                        if lang.get('reading'):
                            level_info.append(f"Reading: {lang['reading']}")
                        if lang.get('writing'):
                            level_info.append(f"Writing: {lang['writing']}")
                        if lang.get('speaking'):
                            level_info.append(f"Speaking: {lang['speaking']}")
                        
                        lang_text = lang['name']
                        if level_info:
                            lang_text += f" ({', '.join(level_info)})"
                        
                        story.append(Paragraph(lang_text, styles['BodyText']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'hobbies':
            if data.get('hobbies'):
                story.append(Paragraph('PASSIONS', styles['SectionTitle']))
                hobbies_list = [hobby.strip() for hobby in data['hobbies'].split(',')]
                for hobby in hobbies_list:
                    if hobby:
                        story.append(Paragraph(f"⭐ {hobby}", styles['BodyText']))
                story.append(Spacer(1, 0.1*inch))

    # Build the document
    doc.build(story)
    buffer.seek(0)
    return buffer