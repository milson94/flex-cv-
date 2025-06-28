import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, gray, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=0.75*inch, leftMargin=0.75*inch,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)

    styles = getSampleStyleSheet()

    # --- Custom Styles ---
    styles.add(ParagraphStyle(name='NameHeader',
                              fontName='Helvetica-Bold',
                              fontSize=28,
                              leading=32,
                              alignment=TA_LEFT,
                              textColor=HexColor('#2C3E50'),
                              spaceAfter=0.1*inch))

    styles.add(ParagraphStyle(name='TitleHeader',
                              fontName='Helvetica',
                              fontSize=14,
                              leading=16,
                              alignment=TA_LEFT,
                              textColor=HexColor('#2980B9'),
                              spaceAfter=0.2*inch))

    styles.add(ParagraphStyle(name='ContactHeader',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              alignment=TA_LEFT,
                              spaceAfter=0.3*inch))

    styles.add(ParagraphStyle(name='SectionTitle',
                              fontName='Helvetica-Bold',
                              fontSize=14,
                              leading=18,
                              spaceBefore=0.2*inch,
                              spaceAfter=0.1*inch,
                              textColor=HexColor('#2980B9')))

    styles.add(ParagraphStyle(name='JobTitle',
                              fontName='Helvetica-Bold',
                              fontSize=12,
                              leading=15,
                              textColor=HexColor('#2C3E50')))

    styles.add(ParagraphStyle(name='CompanyDate',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              textColor=HexColor('#7F8C8D'),
                              spaceAfter=0.05*inch))

    styles.add(ParagraphStyle(name='BulletPoint',
                              parent=styles['Normal'],
                              leftIndent=0.25*inch,
                              bulletIndent=0.1*inch,
                              firstLineIndent=0,
                              spaceBefore=0.05*inch))

    styles.add(ParagraphStyle(name='NormalIndented',
                              parent=styles['Normal'],
                              leftIndent=0.25*inch))

    styles.add(ParagraphStyle(name='NormalJustified',
                              parent=styles['Normal'],
                              alignment=TA_JUSTIFY))

    styles.add(ParagraphStyle(name='AchievementTitle',
                              fontName='Helvetica-Bold',
                              fontSize=11,
                              leading=14,
                              textColor=HexColor('#2C3E50')))

    styles.add(ParagraphStyle(name='AchievementDesc',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              textColor=HexColor('#7F8C8D'),
                              spaceAfter=0.1*inch))

    story = []

    # --- Header Section ---
    if data.get('full_name'):
        story.append(Paragraph(data['full_name'].upper(), styles['NameHeader']))

    if data.get('title_subtitle'):
        story.append(Paragraph(data['title_subtitle'], styles['TitleHeader']))

    # Contact information
    contact_info = []
    if data.get('phone'): contact_info.append(f"📞 {data['phone']}")
    if data.get('email'): contact_info.append(f"✉ {data['email']}")
    if data.get('linkedin'): contact_info.append(f"🔗 {data['linkedin']}")
    if data.get('location'): contact_info.append(f"📍 {data['location']}")
    
    if contact_info:
        story.append(Paragraph(" | ".join(contact_info), styles['ContactHeader']))

    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#2980B9'), 
                           spaceBefore=0.1*inch, spaceAfter=0.2*inch))

    # Get section order from data, with fallback to default
    section_order = data.get('section_order', ['summary', 'experience', 'education', 'achievements', 'courses', 'skills', 'hobbies', 'languages'])

    # Process sections in the specified order
    for section_key in section_order:
        if section_key == 'summary':
            if data.get('summary'):
                story.append(Paragraph("SUMMARY", styles['SectionTitle']))
                story.append(Paragraph(data['summary'], styles['NormalJustified']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'experience':
            experiences = data.get('experiences', [])
            if experiences:
                story.append(Paragraph("EXPERIENCE", styles['SectionTitle']))
                for exp in experiences:
                    if exp.get('title') and exp.get('company'):
                        story.append(Paragraph(exp['title'], styles['JobTitle']))
                        
                        # Build company/date line
                        company_line = exp['company']
                        if exp.get('location'):
                            company_line += f" | {exp['location']}"
                        
                        # Add dates
                        if exp.get('start_date'):
                            company_line += f" | {exp['start_date']}"
                            if exp.get('end_date'):
                                company_line += f" - {exp['end_date']}"
                            elif exp.get('is_present'):
                                company_line += " - Present"
                        
                        story.append(Paragraph(company_line, styles['CompanyDate']))
                        
                        if exp.get('description'):
                            desc_lines = exp['description'].split('\n')
                            for line in desc_lines:
                                line = line.strip()
                                if line.startswith(('-', '*', '•')):
                                    story.append(Paragraph(f"• {line[1:].strip()}", styles['BulletPoint']))
                                elif line:
                                    story.append(Paragraph(line, styles['NormalIndented']))
                        story.append(Spacer(1, 0.15*inch))

        elif section_key == 'education':
            education_entries = data.get('education_entries', [])
            if education_entries:
                story.append(Paragraph("EDUCATION", styles['SectionTitle']))
                for edu in education_entries:
                    if edu.get('degree') and edu.get('institution'):
                        story.append(Paragraph(edu['degree'], styles['JobTitle']))
                        
                        # Build institution/date line
                        edu_line = edu['institution']
                        if edu.get('edu_location'):
                            edu_line += f" | {edu['edu_location']}"
                        
                        # Add dates
                        if edu.get('start_date'):
                            edu_line += f" | {edu['start_date']}"
                            if edu.get('end_date'):
                                edu_line += f" - {edu['end_date']}"
                            elif edu.get('is_present'):
                                edu_line += " - Present"
                        
                        story.append(Paragraph(edu_line, styles['CompanyDate']))
                        
                        if edu.get('edu_details'):
                            story.append(Paragraph(edu['edu_details'], styles['NormalIndented']))
                        story.append(Spacer(1, 0.1*inch))

        elif section_key == 'achievements':
            key_achievements = data.get('key_achievements', [])
            if key_achievements:
                story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionTitle']))
                for achievement in key_achievements:
                    if achievement.get('title'):
                        story.append(Paragraph(f"🏆 {achievement['title']}", styles['AchievementTitle']))
                        if achievement.get('description'):
                            story.append(Paragraph(achievement['description'], styles['AchievementDesc']))

        elif section_key == 'courses':
            courses = data.get('courses', [])
            if courses:
                story.append(Paragraph("COURSES", styles['SectionTitle']))
                for course in courses:
                    if course.get('title'):
                        story.append(Paragraph(course['title'], styles['AchievementTitle']))
                        if course.get('description'):
                            story.append(Paragraph(course['description'], styles['AchievementDesc']))

        elif section_key == 'skills':
            if data.get('skills'):
                story.append(Paragraph("SKILLS", styles['SectionTitle']))
                
                # Create a simple table for skills
                skills_list = [skill.strip() for skill in data['skills'].split(',')]
                skills_table_data = []
                row = []
                
                for i, skill in enumerate(skills_list):
                    if skill:
                        row.append(skill)
                        if len(row) == 3 or i == len(skills_list) - 1:  # 3 skills per row
                            # Pad row if needed
                            while len(row) < 3:
                                row.append('')
                            skills_table_data.append(row)
                            row = []
                
                if skills_table_data:
                    skills_table = Table(skills_table_data, style=[
                        ('VALIGN', (0,0), (-1,-1), 'TOP'),
                        ('LEFTPADDING', (0,0), (-1,-1), 8),
                        ('RIGHTPADDING', (0,0), (-1,-1), 8),
                        ('TOPPADDING', (0,0), (-1,-1), 6),
                        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                        ('BACKGROUND', (0,0), (-1,-1), HexColor('#F8F9FA')),
                        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#E9ECEF')),
                        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
                        ('FONTSIZE', (0,0), (-1,-1), 10)
                    ])
                    story.append(skills_table)
                    story.append(Spacer(1, 0.1*inch))

        elif section_key == 'hobbies':
            if data.get('hobbies'):
                story.append(Paragraph("PASSIONS", styles['SectionTitle']))
                hobbies_list = [hobby.strip() for hobby in data['hobbies'].split(',')]
                for hobby in hobbies_list:
                    if hobby:
                        story.append(Paragraph(f"⭐ {hobby}", styles['AchievementDesc']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'languages':
            languages = data.get('languages', [])
            if languages:
                story.append(Paragraph("LANGUAGES", styles['SectionTitle']))
                for lang in languages:
                    if lang.get('name'):
                        level = lang.get('level', 'Conversational')
                        story.append(Paragraph(f"{lang['name']}: {level}", styles['AchievementDesc']))
                story.append(Spacer(1, 0.1*inch))

    doc.build(story)
    buffer.seek(0)
    return buffer