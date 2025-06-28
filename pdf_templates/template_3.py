import io
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, FrameBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter

# Color palette matching the template image
COLOR_SIDEBAR_BG = HexColor('#2C5282')  # Dark blue sidebar
COLOR_SIDEBAR_TEXT = white
COLOR_MAIN_TEXT = HexColor('#333333')
COLOR_ACCENT_BLUE = HexColor('#3182CE')
COLOR_LIGHT_GRAY = HexColor('#F7FAFC')

class ModernTwoColumnDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Define frame dimensions
        sidebar_width = 2.5 * inch
        main_width = self.width - sidebar_width
        
        # Create frames
        frame_sidebar = Frame(
            self.leftMargin, self.bottomMargin,
            sidebar_width, self.height,
            id='sidebar', showBoundary=0,
            leftPadding=0.3*inch, rightPadding=0.2*inch,
            topPadding=0.3*inch, bottomPadding=0.3*inch
        )
        
        frame_main = Frame(
            self.leftMargin + sidebar_width, self.bottomMargin,
            main_width, self.height,
            id='main', showBoundary=0,
            leftPadding=0.3*inch, rightPadding=0.3*inch,
            topPadding=0.3*inch, bottomPadding=0.3*inch
        )
        
        # Create page template
        page_template = PageTemplate(
            id='TwoColumn', 
            frames=[frame_sidebar, frame_main],
            onPage=self.draw_background
        )
        self.addPageTemplates([page_template])
    
    def draw_background(self, canvas, doc):
        """Draw the sidebar background"""
        canvas.saveState()
        
        # Draw sidebar background
        sidebar_width = 2.5 * inch
        canvas.setFillColor(COLOR_SIDEBAR_BG)
        canvas.rect(
            doc.leftMargin, 0,
            sidebar_width, doc.pagesize[1],
            stroke=0, fill=1
        )
        
        canvas.restoreState()

def generate_pdf(data):
    buffer = io.BytesIO()
    
    doc = ModernTwoColumnDocTemplate(
        buffer, pagesize=letter,
        leftMargin=0, rightMargin=0.5*inch,
        topMargin=0.5*inch, bottomMargin=0.5*inch
    )
    
    styles = getSampleStyleSheet()
    
    # Define custom styles for sidebar
    styles.add(ParagraphStyle(
        name='SidebarName',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=COLOR_SIDEBAR_TEXT,
        spaceAfter=0.3*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='SidebarSectionTitle',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=COLOR_SIDEBAR_TEXT,
        spaceBefore=0.2*inch,
        spaceAfter=0.1*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='SidebarText',
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=COLOR_SIDEBAR_TEXT,
        spaceAfter=0.05*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='SidebarBullet',
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=COLOR_SIDEBAR_TEXT,
        leftIndent=0.1*inch,
        spaceAfter=0.03*inch,
        alignment=TA_LEFT
    ))
    
    # Define custom styles for main content
    styles.add(ParagraphStyle(
        name='MainTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=COLOR_ACCENT_BLUE,
        spaceAfter=0.05*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='MainSubtitle',
        fontName='Helvetica',
        fontSize=12,
        leading=14,
        textColor=COLOR_MAIN_TEXT,
        spaceAfter=0.1*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='ContactInfo',
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=COLOR_MAIN_TEXT,
        spaceAfter=0.2*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='MainSectionTitle',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=COLOR_MAIN_TEXT,
        spaceBefore=0.2*inch,
        spaceAfter=0.1*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='JobTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=COLOR_MAIN_TEXT,
        spaceAfter=0.02*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='CompanyDate',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_ACCENT_BLUE,
        spaceAfter=0.05*inch,
        alignment=TA_LEFT
    ))
    
    styles.add(ParagraphStyle(
        name='MainText',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_MAIN_TEXT,
        spaceAfter=0.05*inch,
        alignment=TA_JUSTIFY
    ))
    
    styles.add(ParagraphStyle(
        name='MainBullet',
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=COLOR_MAIN_TEXT,
        leftIndent=0.15*inch,
        spaceAfter=0.03*inch,
        alignment=TA_LEFT
    ))
    
    # Build sidebar content
    sidebar_story = []
    
    # Name
    if data.get('full_name'):
        sidebar_story.append(Paragraph(data['full_name'].upper(), styles['SidebarName']))
    
    # Key Achievements
    key_achievements = data.get('key_achievements', [])
    if key_achievements:
        sidebar_story.append(Paragraph("KEY ACHIEVEMENTS", styles['SidebarSectionTitle']))
        for achievement in key_achievements:
            if achievement.get('title'):
                sidebar_story.append(Paragraph(f"🔧 {achievement['title']}", styles['SidebarText']))
                if achievement.get('description'):
                    sidebar_story.append(Paragraph(achievement['description'], styles['SidebarText']))
                sidebar_story.append(Spacer(1, 0.1*inch))
    
    # Certification/Courses
    courses = data.get('courses', [])
    if courses:
        sidebar_story.append(Paragraph("CERTIFICATION", styles['SidebarSectionTitle']))
        for course in courses:
            if course.get('title'):
                sidebar_story.append(Paragraph(course['title'], styles['SidebarText']))
                if course.get('description'):
                    sidebar_story.append(Paragraph(course['description'], styles['SidebarText']))
                sidebar_story.append(Spacer(1, 0.05*inch))
    
    # Skills
    if data.get('skills'):
        sidebar_story.append(Paragraph("SKILLS", styles['SidebarSectionTitle']))
        skills_list = [skill.strip() for skill in data['skills'].split(',')]
        for skill in skills_list[:10]:  # Limit to first 10 skills
            if skill:
                sidebar_story.append(Paragraph(f"• {skill}", styles['SidebarBullet']))
    
    # Languages
    languages = data.get('languages', [])
    if languages:
        sidebar_story.append(Paragraph("LANGUAGES", styles['SidebarSectionTitle']))
        for lang in languages:
            if lang.get('name'):
                level = lang.get('level', 'Conversational')
                sidebar_story.append(Paragraph(f"{lang['name']}: {level}", styles['SidebarText']))
    
    # Hobbies/Passions
    if data.get('hobbies'):
        sidebar_story.append(Paragraph("PASSIONS", styles['SidebarSectionTitle']))
        hobbies_list = [hobby.strip() for hobby in data['hobbies'].split(',')]
        for hobby in hobbies_list[:5]:  # Limit to first 5 hobbies
            if hobby:
                sidebar_story.append(Paragraph(f"🌟 {hobby}", styles['SidebarText']))
    
    # Build main content
    main_story = []
    
    # Title and contact info
    if data.get('title_subtitle'):
        main_story.append(Paragraph(data['title_subtitle'], styles['MainTitle']))
    
    # Contact information
    contact_info = []
    if data.get('email'): contact_info.append(f"📧 {data['email']}")
    if data.get('linkedin'): contact_info.append(f"🔗 {data['linkedin']}")
    if data.get('location'): contact_info.append(f"📍 {data['location']}")
    
    if contact_info:
        main_story.append(Paragraph(" | ".join(contact_info), styles['ContactInfo']))
    
    # Summary
    if data.get('summary'):
        main_story.append(Paragraph("SUMMARY", styles['MainSectionTitle']))
        main_story.append(Paragraph(data['summary'], styles['MainText']))
        main_story.append(Spacer(1, 0.1*inch))
    
    # Experience
    experiences = data.get('experiences', [])
    if experiences:
        main_story.append(Paragraph("EXPERIENCE", styles['MainSectionTitle']))
        for exp in experiences:
            if exp.get('title') and exp.get('company'):
                main_story.append(Paragraph(exp['title'], styles['JobTitle']))
                
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
                
                main_story.append(Paragraph(company_info, styles['CompanyDate']))
                
                # Description
                if exp.get('description'):
                    desc_lines = exp['description'].split('\n')
                    for line in desc_lines:
                        line = line.strip()
                        if line.startswith(('-', '*', '•')):
                            main_story.append(Paragraph(f"• {line[1:].strip()}", styles['MainBullet']))
                        elif line:
                            main_story.append(Paragraph(line, styles['MainText']))
                
                main_story.append(Spacer(1, 0.15*inch))
    
    # Education
    education_entries = data.get('education_entries', [])
    if education_entries:
        main_story.append(Paragraph("EDUCATION", styles['MainSectionTitle']))
        for edu in education_entries:
            if edu.get('degree') and edu.get('institution'):
                main_story.append(Paragraph(edu['degree'], styles['JobTitle']))
                
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
                
                main_story.append(Paragraph(edu_info, styles['CompanyDate']))
                
                if edu.get('edu_details'):
                    main_story.append(Paragraph(edu['edu_details'], styles['MainText']))
                
                main_story.append(Spacer(1, 0.1*inch))
    
    # Combine stories
    full_story = []
    full_story.extend(sidebar_story)
    full_story.append(FrameBreak())  # Move to main content frame
    full_story.extend(main_story)
    
    # Build the document
    doc.build(full_story)
    buffer.seek(0)
    return buffer