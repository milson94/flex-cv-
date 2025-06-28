import io
import os
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, FrameBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter

# Color palette matching the template
COLOR_HEADER_BG = HexColor('#2C3E50')  # Dark blue-grey header
COLOR_HEADER_TEXT = white
COLOR_SECTION_TITLE = HexColor('#2980B9')  # Blue for section titles
COLOR_TEXT_MAIN = HexColor('#2C3E50')
COLOR_TEXT_MUTED = HexColor('#7F8C8D')
COLOR_ACCENT = HexColor('#3498DB')

class ProfessionalDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        self.profile_image_path = kwargs.pop('profile_image_path', None)
        self.resume_data = kwargs.pop('resume_data', {})
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Header height
        header_height = 1.8 * inch
        
        # Define frame dimensions for two-column layout below header
        left_col_width = self.width * 0.55  # Left column slightly wider
        right_col_width = self.width * 0.40  # Right column
        gap = self.width - left_col_width - right_col_width
        
        # Create frames starting below the header
        frame_left = Frame(
            self.leftMargin, self.bottomMargin,
            left_col_width, self.height - header_height,
            id='col_left', showBoundary=0,
            leftPadding=0, rightPadding=gap/2,
            topPadding=0.2*inch, bottomPadding=0
        )
        
        frame_right = Frame(
            self.leftMargin + left_col_width + gap, self.bottomMargin,
            right_col_width, self.height - header_height,
            id='col_right', showBoundary=0,
            leftPadding=gap/2, rightPadding=0,
            topPadding=0.2*inch, bottomPadding=0
        )
        
        # Create page template
        page_template = PageTemplate(
            id='Professional', 
            frames=[frame_left, frame_right],
            onPage=self.draw_header
        )
        self.addPageTemplates([page_template])
    
    def draw_header(self, canvas, doc):
        """Draw the header with name, title, contact info and profile photo"""
        canvas.saveState()
        
        # Header background
        header_height = 1.8 * inch
        canvas.setFillColor(COLOR_HEADER_BG)
        canvas.rect(0, doc.pagesize[1] - header_height, doc.pagesize[0], header_height, stroke=0, fill=1)
        
        # Profile image (top right of header)
        if self.profile_image_path and os.path.exists(self.profile_image_path):
            try:
                img_size = 1.2 * inch
                img_x = doc.pagesize[0] - doc.rightMargin - img_size - 0.3*inch
                img_y = doc.pagesize[1] - header_height + (header_height - img_size) / 2
                
                # Circular clipping
                path = canvas.beginPath()
                path.circle(img_x + img_size/2, img_y + img_size/2, img_size/2)
                canvas.clipPath(path, stroke=0, fill=0)
                canvas.drawImage(self.profile_image_path, img_x, img_y, width=img_size, height=img_size, mask='auto')
            except Exception as e:
                print(f"Error drawing profile image: {e}")
        
        canvas.restoreState()
        canvas.saveState()
        
        # Header text content
        canvas.setFillColor(COLOR_HEADER_TEXT)
        
        # Name
        if self.resume_data.get('full_name'):
            canvas.setFont('Helvetica-Bold', 28)
            canvas.drawString(doc.leftMargin, doc.pagesize[1] - 0.6*inch, self.resume_data['full_name'].upper())
        
        # Title/Subtitle
        if self.resume_data.get('title_subtitle'):
            canvas.setFont('Helvetica', 14)
            canvas.drawString(doc.leftMargin, doc.pagesize[1] - 0.9*inch, self.resume_data['title_subtitle'])
        
        # Contact info
        contact_y = doc.pagesize[1] - 1.3*inch
        canvas.setFont('Helvetica', 10)
        contact_items = []
        
        if self.resume_data.get('phone'):
            contact_items.append(f"📞 {self.resume_data['phone']}")
        if self.resume_data.get('email'):
            contact_items.append(f"✉ {self.resume_data['email']}")
        if self.resume_data.get('linkedin'):
            contact_items.append(f"🔗 {self.resume_data['linkedin']}")
        if self.resume_data.get('location'):
            contact_items.append(f"📍 {self.resume_data['location']}")
        
        # Draw contact items in rows
        x_pos = doc.leftMargin
        y_pos = contact_y
        items_per_row = 2
        
        for i, item in enumerate(contact_items):
            if i > 0 and i % items_per_row == 0:
                y_pos -= 0.2*inch
                x_pos = doc.leftMargin
            canvas.drawString(x_pos, y_pos, item)
            x_pos += 3*inch  # Space between items
        
        canvas.restoreState()

def generate_pdf(data):
    buffer = io.BytesIO()
    
    doc = ProfessionalDocTemplate(
        buffer, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.5*inch, bottomMargin=0.75*inch,
        profile_image_path=data.get('profile_image_path'),
        resume_data=data
    )
    
    styles = getSampleStyleSheet()
    
    # Define custom styles
    styles.add(ParagraphStyle(
        name='SectionTitleLeft',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=COLOR_SECTION_TITLE,
        spaceBefore=0.2*inch,
        spaceAfter=0.1*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='SectionTitleRight',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=COLOR_SECTION_TITLE,
        spaceBefore=0.2*inch,
        spaceAfter=0.1*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='JobTitle',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=COLOR_TEXT_MAIN,
        spaceAfter=0.02*inch
    ))
    
    styles.add(ParagraphStyle(
        name='CompanyDate',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_TEXT_MUTED,
        spaceAfter=0.05*inch
    ))
    
    styles.add(ParagraphStyle(
        name='BodyText',
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=COLOR_TEXT_MAIN,
        alignment=TA_JUSTIFY,
        spaceAfter=0.05*inch
    ))
    
    styles.add(ParagraphStyle(
        name='BulletPoint',
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=COLOR_TEXT_MAIN,
        leftIndent=0.15*inch,
        spaceAfter=0.03*inch
    ))
    
    styles.add(ParagraphStyle(
        name='SkillItem',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_TEXT_MAIN,
        spaceAfter=0.05*inch
    ))
    
    styles.add(ParagraphStyle(
        name='AchievementTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_TEXT_MAIN,
        spaceAfter=0.02*inch
    ))
    
    styles.add(ParagraphStyle(
        name='AchievementDesc',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_TEXT_MUTED,
        spaceAfter=0.1*inch
    ))
    
    # Build left column content
    left_story = []
    
    # EXPERIENCE
    experiences = data.get('experiences', [])
    if experiences:
        left_story.append(Paragraph("EXPERIENCE", styles['SectionTitleLeft']))
        for exp in experiences:
            if exp.get('title') and exp.get('company'):
                left_story.append(Paragraph(exp['title'], styles['JobTitle']))
                
                # Company and dates
                company_info = exp['company']
                if exp.get('location'):
                    company_info += f" | {exp['location']}"
                
                date_range = ""
                if exp.get('start_date'):
                    date_range = exp['start_date']
                    if exp.get('end_date'):
                        date_range += f" - {exp['end_date']}"
                    elif exp.get('is_present'):
                        date_range += " - Present"
                
                if date_range:
                    company_info += f" | {date_range}"
                
                left_story.append(Paragraph(company_info, styles['CompanyDate']))
                
                # Description
                if exp.get('description'):
                    desc_lines = exp['description'].split('\n')
                    for line in desc_lines:
                        line = line.strip()
                        if line.startswith(('-', '*', '•')):
                            left_story.append(Paragraph(f"• {line[1:].strip()}", styles['BulletPoint']))
                        elif line:
                            left_story.append(Paragraph(line, styles['BodyText']))
                
                left_story.append(Spacer(1, 0.15*inch))
    
    # EDUCATION
    education_entries = data.get('education_entries', [])
    if education_entries:
        left_story.append(Paragraph("EDUCATION", styles['SectionTitleLeft']))
        for edu in education_entries:
            if edu.get('degree') and edu.get('institution'):
                left_story.append(Paragraph(edu['degree'], styles['JobTitle']))
                
                # Institution and dates
                edu_info = edu['institution']
                if edu.get('edu_location'):
                    edu_info += f" | {edu['edu_location']}"
                
                date_range = ""
                if edu.get('start_date'):
                    date_range = edu['start_date']
                    if edu.get('end_date'):
                        date_range += f" - {edu['end_date']}"
                    elif edu.get('is_present'):
                        date_range += " - Present"
                
                if date_range:
                    edu_info += f" | {date_range}"
                
                left_story.append(Paragraph(edu_info, styles['CompanyDate']))
                
                if edu.get('edu_details'):
                    left_story.append(Paragraph(edu['edu_details'], styles['BodyText']))
                
                left_story.append(Spacer(1, 0.1*inch))
    
    # SKILLS
    if data.get('skills'):
        left_story.append(Paragraph("SKILLS", styles['SectionTitleLeft']))
        
        # Create skill boxes/tags
        skills_list = [skill.strip() for skill in data['skills'].split(',')]
        skills_table_data = []
        row = []
        
        for i, skill in enumerate(skills_list):
            if skill:
                row.append(Paragraph(skill, styles['SkillItem']))
                if len(row) == 3 or i == len(skills_list) - 1:  # 3 skills per row
                    skills_table_data.append(row)
                    row = []
        
        if skills_table_data:
            skills_table = Table(skills_table_data, style=[
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 5),
                ('RIGHTPADDING', (0,0), (-1,-1), 5),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('BACKGROUND', (0,0), (-1,-1), HexColor('#F8F9FA')),
                ('GRID', (0,0), (-1,-1), 0.5, HexColor('#E9ECEF'))
            ])
            left_story.append(skills_table)
            left_story.append(Spacer(1, 0.1*inch))
    
    # Build right column content
    right_story = []
    
    # SUMMARY
    if data.get('summary'):
        right_story.append(Paragraph("SUMMARY", styles['SectionTitleRight']))
        right_story.append(Paragraph(data['summary'], styles['BodyText']))
        right_story.append(Spacer(1, 0.15*inch))
    
    # KEY ACHIEVEMENTS
    key_achievements = data.get('key_achievements', [])
    if key_achievements:
        right_story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionTitleRight']))
        for achievement in key_achievements:
            if achievement.get('title'):
                right_story.append(Paragraph(f"🏆 {achievement['title']}", styles['AchievementTitle']))
                if achievement.get('description'):
                    right_story.append(Paragraph(achievement['description'], styles['AchievementDesc']))
        right_story.append(Spacer(1, 0.15*inch))
    
    # COURSES
    courses = data.get('courses', [])
    if courses:
        right_story.append(Paragraph("COURSES", styles['SectionTitleRight']))
        for course in courses:
            if course.get('title'):
                right_story.append(Paragraph(course['title'], styles['AchievementTitle']))
                if course.get('description'):
                    right_story.append(Paragraph(course['description'], styles['AchievementDesc']))
        right_story.append(Spacer(1, 0.15*inch))
    
    # PASSIONS/HOBBIES
    if data.get('hobbies'):
        right_story.append(Paragraph("PASSIONS", styles['SectionTitleRight']))
        hobbies_list = [hobby.strip() for hobby in data['hobbies'].split(',')]
        for hobby in hobbies_list:
            if hobby:
                right_story.append(Paragraph(f"⭐ {hobby}", styles['AchievementDesc']))
        right_story.append(Spacer(1, 0.15*inch))
    
    # LANGUAGES
    languages = data.get('languages', [])
    if languages:
        right_story.append(Paragraph("LANGUAGES", styles['SectionTitleRight']))
        for lang in languages:
            if lang.get('name'):
                level = lang.get('level', 'Conversational')
                right_story.append(Paragraph(f"{lang['name']}: {level}", styles['AchievementDesc']))
    
    # Combine stories
    full_story = []
    full_story.extend(left_story)
    full_story.append(FrameBreak())  # Move to right column
    full_story.extend(right_story)
    
    # Build the document
    doc.build(full_story)
    buffer.seek(0)
    return buffer