import io
import os
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, FrameBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# --- Color Palette matching Elise Carter template ---
COLOR_TEXT_MAIN = HexColor('#333333')
COLOR_TEXT_MUTED = HexColor('#666666')
COLOR_TEXT_HEADER = HexColor('#2c3e50')
COLOR_ACCENT_GREEN = HexColor('#16a085')  # Teal/green accent
COLOR_SECTION_GREEN = HexColor('#4CAF50')  # Green for section titles
COLOR_BACKGROUND_LIGHT = HexColor('#f8f9fa')

class EliseCarterDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        self.profile_image_path = kwargs.pop('profile_image_path', None)
        BaseDocTemplate.__init__(self, filename, **kwargs)

        # Define Frames: Main content (left), sidebar (right)
        main_col_width = self.width * 0.65  # Main content takes 65%
        sidebar_width = self.width * 0.30   # Sidebar takes 30%
        gap = self.width - main_col_width - sidebar_width  # Small gap

        # Main content frame (left side)
        frame_main = Frame(self.leftMargin, self.bottomMargin,
                           main_col_width, self.height, id='col_main', showBoundary=0,
                           leftPadding=0, rightPadding=12, topPadding=0, bottomPadding=0)
        
        # Sidebar frame (right side)
        frame_sidebar = Frame(self.leftMargin + main_col_width + gap, self.bottomMargin,
                              sidebar_width, self.height, id='col_sidebar', showBoundary=0,
                              leftPadding=12, rightPadding=0, topPadding=0, bottomPadding=0)
        
        main_page = PageTemplate(id='MainPageElise', frames=[frame_main, frame_sidebar], 
                                onPage=self.draw_header_and_profile)
        self.addPageTemplates([main_page])

    def draw_header_and_profile(self, canvas, doc):
        """Draw the profile image in the top-right corner"""
        canvas.saveState()
        
        # Profile Image (Top Right corner of the page)
        if self.profile_image_path and os.path.exists(self.profile_image_path):
            try:
                img_size = 1.5 * inch
                # Position in the absolute top-right corner
                img_x = doc.pagesize[0] - doc.rightMargin - img_size - 0.1*inch
                img_y = doc.pagesize[1] - doc.topMargin - img_size - 0.1*inch
                
                # Create circular clipping path
                center_x = img_x + img_size/2
                center_y = img_y + img_size/2
                radius = img_size/2
                
                path = canvas.beginPath()
                path.circle(center_x, center_y, radius)
                canvas.clipPath(path, stroke=0, fill=0)
                
                # Draw the image
                canvas.drawImage(self.profile_image_path, img_x, img_y, 
                               width=img_size, height=img_size, mask='auto')
                
            except Exception as e:
                print(f"Error drawing profile image: {e}")
                # Draw a placeholder circle if image fails
                canvas.setFillColor(HexColor('#E0E0E0'))
                canvas.circle(center_x, center_y, radius, stroke=1, fill=1)
        
        canvas.restoreState()


def generate_pdf(data):
    buffer = io.BytesIO()
    
    doc = EliseCarterDocTemplate(buffer, pagesize=letter,
                                 leftMargin=0.75*inch, rightMargin=0.75*inch,
                                 topMargin=0.75*inch, bottomMargin=0.75*inch,
                                 profile_image_path=data.get('profile_image_path'))

    styles = getSampleStyleSheet()
    
    # --- Define Styles matching Elise Carter template ---
    styles.add(ParagraphStyle(name='FullName', fontName='Helvetica-Bold', fontSize=28, 
                              textColor=COLOR_TEXT_HEADER, spaceBefore=0, leading=32, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='JobTitleHeader', fontName='Helvetica', fontSize=12, 
                              textColor=COLOR_TEXT_MAIN, spaceAfter=6, leading=15))
    styles.add(ParagraphStyle(name='ContactInfo', fontName='Helvetica', fontSize=9, 
                              textColor=COLOR_TEXT_MUTED, leading=12, spaceAfter=0.15*inch))

    # Main content styles
    styles.add(ParagraphStyle(name='MainSectionTitle', fontName='Helvetica-Bold', fontSize=11, 
                              textColor=COLOR_SECTION_GREEN, spaceBefore=0.2*inch, spaceAfter=0.08*inch, 
                              leading=13, alignment=TA_LEFT, textTransform='uppercase'))
    styles.add(ParagraphStyle(name='MainBodyText', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=14, spaceAfter=4, alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='ExpJobTitle', fontName='Helvetica-Bold', fontSize=12, 
                              textColor=COLOR_TEXT_MAIN, leading=15, spaceAfter=2))
    styles.add(ParagraphStyle(name='ExpCompanyDate', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MUTED, leading=13, spaceAfter=4))
    styles.add(ParagraphStyle(name='ExpBullet', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=13, leftIndent=15, 
                              firstLineIndent=0, spaceBefore=2, bulletIndent=5))
    styles.add(ParagraphStyle(name='EduDegree', fontName='Helvetica-Bold', fontSize=11, 
                              textColor=COLOR_TEXT_MAIN, leading=14, spaceAfter=2))
    styles.add(ParagraphStyle(name='EduInstitutionDate', fontName='Helvetica', fontSize=10, 
                              textColor=COLOR_TEXT_MUTED, leading=13, spaceAfter=4))

    # Sidebar styles
    styles.add(ParagraphStyle(name='SidebarSectionTitle', fontName='Helvetica-Bold', fontSize=10, 
                              textColor=COLOR_SECTION_GREEN, spaceBefore=0.25*inch, spaceAfter=0.1*inch, 
                              leading=12, textTransform='uppercase'))
    styles.add(ParagraphStyle(name='SidebarItemTitle', fontName='Helvetica-Bold', fontSize=10, 
                              textColor=COLOR_TEXT_MAIN, leading=13, spaceAfter=2))
    styles.add(ParagraphStyle(name='SidebarItemDesc', fontName='Helvetica', fontSize=9, 
                              textColor=COLOR_TEXT_MUTED, leading=12, spaceAfter=0.12*inch))
    styles.add(ParagraphStyle(name='SidebarSkill', fontName='Helvetica', fontSize=9, 
                              textColor=COLOR_TEXT_MAIN, leading=12, spaceAfter=3))

    # --- Story for Main Column (Left) ---
    story_main = []
    
    # Header section (Name, Title, Contact)
    if data.get('full_name'):
        story_main.append(Paragraph(data['full_name'].upper(), styles['FullName']))
    if data.get('title_subtitle'):
        story_main.append(Paragraph(data['title_subtitle'], styles['JobTitleHeader']))
    
    contact_items = []
    if data.get('email'): contact_items.append(f"@ {data['email']}")
    if data.get('linkedin'): contact_items.append(f"🔗 {data['linkedin']}")
    if data.get('location'): contact_items.append(f"📍 {data['location']}")
    if contact_items:
        story_main.append(Paragraph("  ".join(contact_items), styles['ContactInfo']))
    
    story_main.append(Spacer(1, 0.2*inch))

    # Get section order from data
    section_order = data.get('section_order', ['summary', 'experience', 'education'])

    for section_key in section_order:
        if section_key == 'summary':
            if data.get('summary'):
                story_main.append(Paragraph('SUMMARY', styles['MainSectionTitle']))
                story_main.append(Paragraph(data['summary'], styles['MainBodyText']))
                story_main.append(Spacer(1, 0.15*inch))

        elif section_key == 'experience':
            experiences = data.get('experiences', [])
            if experiences:
                story_main.append(Paragraph('EXPERIENCE', styles['MainSectionTitle']))
                for exp in experiences:
                    if exp.get('title'):
                        story_main.append(Paragraph(exp['title'], styles['ExpJobTitle']))
                    
                    # Company and dates line
                    company_date_parts = []
                    if exp.get('company'):
                        company_date_parts.append(exp['company'])
                    
                    # Format dates
                    if exp.get('start_date'):
                        date_str = exp['start_date']
                        if exp.get('end_date'):
                            date_str += f" - {exp['end_date']}"
                        elif exp.get('is_present'):
                            date_str += " - Present"
                        company_date_parts.append(f"📅 {date_str}")
                    
                    if exp.get('location'):
                        company_date_parts.append(f"📍 {exp['location']}")
                    
                    if company_date_parts:
                        story_main.append(Paragraph("  ".join(company_date_parts), styles['ExpCompanyDate']))
                    
                    # Description with bullet points
                    if exp.get('description'):
                        desc_lines = exp['description'].split('\n')
                        for line in desc_lines:
                            line = line.strip()
                            if line:
                                story_main.append(Paragraph(f"• {line}", styles['ExpBullet']))
                    
                    story_main.append(Spacer(1, 0.15*inch))

        elif section_key == 'education':
            education_entries = data.get('education_entries', [])
            if education_entries:
                story_main.append(Paragraph('EDUCATION', styles['MainSectionTitle']))
                for edu in education_entries:
                    if edu.get('degree'):
                        story_main.append(Paragraph(edu['degree'], styles['EduDegree']))
                    
                    # Institution and dates
                    edu_parts = []
                    if edu.get('institution'):
                        edu_parts.append(edu['institution'])
                    
                    if edu.get('start_date'):
                        date_str = edu['start_date']
                        if edu.get('end_date'):
                            date_str += f" - {edu['end_date']}"
                        elif edu.get('is_present'):
                            date_str += " - Present"
                        edu_parts.append(date_str)
                    
                    if edu.get('edu_location'):
                        edu_parts.append(edu['edu_location'])
                    
                    if edu_parts:
                        story_main.append(Paragraph("  ".join(edu_parts), styles['EduInstitutionDate']))
                    
                    if edu.get('edu_details'):
                        story_main.append(Paragraph(edu['edu_details'], styles['MainBodyText']))
                    
                    story_main.append(Spacer(1, 0.1*inch))

        elif section_key == 'achievements':
            key_achievements = data.get('key_achievements', [])
            if key_achievements:
                story_main.append(Paragraph('KEY ACHIEVEMENTS', styles['MainSectionTitle']))
                for ach in key_achievements:
                    if ach.get('title'):
                        story_main.append(Paragraph(f"🏆 {ach['title']}", styles['ExpJobTitle']))
                        if ach.get('description'):
                            story_main.append(Paragraph(ach['description'], styles['MainBodyText']))
                        story_main.append(Spacer(1, 0.1*inch))

        elif section_key == 'courses':
            courses = data.get('courses', [])
            if courses:
                story_main.append(Paragraph('COURSES', styles['MainSectionTitle']))
                for course in courses:
                    if course.get('title'):
                        story_main.append(Paragraph(course['title'], styles['ExpJobTitle']))
                        if course.get('description'):
                            story_main.append(Paragraph(course['description'], styles['MainBodyText']))
                        story_main.append(Spacer(1, 0.1*inch))

    # --- Story for Sidebar (Right) ---
    story_sidebar = []
    
    # Add spacer to clear profile image area
    story_sidebar.append(Spacer(1, 1.8 * inch))

    # STRENGTHS/KEY ACHIEVEMENTS
    key_achievements = data.get('key_achievements', [])
    if key_achievements:
        story_sidebar.append(Paragraph('STRENGTHS', styles['SidebarSectionTitle']))
        for ach in key_achievements:
            if ach.get('title'):
                story_sidebar.append(Paragraph(ach['title'], styles['SidebarItemTitle']))
                if ach.get('description'):
                    story_sidebar.append(Paragraph(ach['description'], styles['SidebarItemDesc']))

    # SKILLS
    if data.get('skills'):
        story_sidebar.append(Paragraph('SKILLS', styles['SidebarSectionTitle']))
        skills_list = [skill.strip() for skill in data['skills'].split(',')]
        
        # Group skills in a clean layout
        for skill in skills_list:
            if skill:
                story_sidebar.append(Paragraph(skill, styles['SidebarSkill']))
        story_sidebar.append(Spacer(1, 0.15*inch))

    # PROJECTS
    projects = data.get('projects', [])
    if projects:
        story_sidebar.append(Paragraph('PROJECTS', styles['SidebarSectionTitle']))
        for proj in projects:
            if proj.get('title'):
                story_sidebar.append(Paragraph(proj['title'], styles['SidebarItemTitle']))
                if proj.get('description'):
                    story_sidebar.append(Paragraph(proj['description'], styles['SidebarItemDesc']))

    # LANGUAGES
    languages = data.get('languages', [])
    if languages:
        story_sidebar.append(Paragraph('LANGUAGES', styles['SidebarSectionTitle']))
        for lang in languages:
            if lang.get('name'):
                level = lang.get('level', 'Conversational')
                story_sidebar.append(Paragraph(f"{lang['name']}: {level}", styles['SidebarSkill']))

    # HOW I SPLIT MY TIME / PASSIONS
    if data.get('hobbies'):
        story_sidebar.append(Paragraph('PASSIONS', styles['SidebarSectionTitle']))
        hobbies_list = [hobby.strip() for hobby in data['hobbies'].split(',')]
        for hobby in hobbies_list:
            if hobby:
                story_sidebar.append(Paragraph(f"⭐ {hobby}", styles['SidebarSkill']))

    # --- Combine Stories for Build ---
    full_story = []
    full_story.extend(story_main)
    full_story.append(FrameBreak())  # Move to the sidebar frame
    full_story.extend(story_sidebar)

    doc.build(full_story)
    buffer.seek(0)
    return buffer