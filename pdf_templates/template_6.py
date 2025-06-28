import io
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, gray, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.utils import ImageReader

def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=0.75*inch, leftMargin=0.75*inch,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)

    styles = getSampleStyleSheet()

    # --- Custom Styles based on the template image ---
    styles.add(ParagraphStyle(name='NameHeader',
                              fontName='Helvetica-Bold',
                              fontSize=28,
                              leading=32,
                              alignment=TA_LEFT,
                              textColor=HexColor('#2C3E50'),
                              spaceAfter=0.05*inch))

    styles.add(ParagraphStyle(name='TitleHeader',
                              fontName='Helvetica',
                              fontSize=14,
                              leading=16,
                              alignment=TA_LEFT,
                              textColor=HexColor('#3498DB'),
                              spaceAfter=0.1*inch))

    styles.add(ParagraphStyle(name='ContactInfo',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              alignment=TA_LEFT,
                              spaceAfter=0.2*inch))

    styles.add(ParagraphStyle(name='SectionTitle',
                              fontName='Helvetica-Bold',
                              fontSize=12,
                              leading=15,
                              spaceBefore=0.2*inch,
                              spaceAfter=0.1*inch,
                              textColor=HexColor('#2C3E50'),
                              textTransform='uppercase'))

    styles.add(ParagraphStyle(name='JobTitle',
                              fontName='Helvetica-Bold',
                              fontSize=11,
                              leading=14,
                              textColor=HexColor('#2C3E50')))

    styles.add(ParagraphStyle(name='CompanyInfo',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              textColor=HexColor('#3498DB'),
                              spaceAfter=0.05*inch))

    styles.add(ParagraphStyle(name='DateLocation',
                              fontName='Helvetica',
                              fontSize=9,
                              leading=11,
                              textColor=HexColor('#7F8C8D'),
                              spaceAfter=0.05*inch))

    styles.add(ParagraphStyle(name='BulletPoint',
                              parent=styles['Normal'],
                              leftIndent=0.25*inch,
                              bulletIndent=0.1*inch,
                              firstLineIndent=0,
                              spaceBefore=0.03*inch,
                              fontSize=10,
                              leading=12))

    styles.add(ParagraphStyle(name='NormalText',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              alignment=TA_JUSTIFY,
                              spaceAfter=0.05*inch))

    styles.add(ParagraphStyle(name='SkillItem',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              spaceAfter=0.03*inch))

    styles.add(ParagraphStyle(name='CertificationTitle',
                              fontName='Helvetica-Bold',
                              fontSize=10,
                              leading=12,
                              textColor=HexColor('#3498DB')))

    styles.add(ParagraphStyle(name='CertificationDesc',
                              fontName='Helvetica',
                              fontSize=9,
                              leading=11,
                              spaceAfter=0.1*inch))

    story = []

    # --- Header with Photo ---
    header_data = []
    
    # Left side: Name, title, contact info
    left_content = []
    if data.get('full_name'):
        left_content.append(Paragraph(data['full_name'].upper(), styles['NameHeader']))
    
    if data.get('title_subtitle'):
        left_content.append(Paragraph(data['title_subtitle'], styles['TitleHeader']))
    
    # Contact information with icons
    contact_items = []
    if data.get('phone'): contact_items.append(f"📞 {data['phone']}")
    if data.get('email'): contact_items.append(f"✉ {data['email']}")
    if data.get('linkedin'): contact_items.append(f"🔗 {data['linkedin']}")
    if data.get('location'): contact_items.append(f"📍 {data['location']}")
    
    if contact_items:
        left_content.append(Paragraph(" | ".join(contact_items), styles['ContactInfo']))

    # Right side: Profile photo
    photo_content = []
    profile_image_path = data.get('profile_image_path')
    if profile_image_path and os.path.exists(profile_image_path):
        try:
            # Create circular profile image
            img = Image(profile_image_path, width=1.5*inch, height=1.5*inch)
            photo_content.append(img)
        except Exception as e:
            print(f"Error loading profile image: {e}")
            # Add placeholder if image fails to load
            photo_content.append(Paragraph("Photo", styles['ContactInfo']))
    else:
        # Add placeholder if no image provided
        photo_content.append(Paragraph("", styles['ContactInfo']))

    # Create header table
    if photo_content and photo_content[0]:
        header_data.append([left_content, photo_content[0]])
        header_table = Table(header_data, colWidths=[5.5*inch, 1.5*inch])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('ALIGN', (1,0), (1,0), 'CENTER'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(header_table)
    else:
        # If no photo, just add the left content
        story.extend(left_content)

    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#BDC3C7'), 
                           spaceBefore=0.1*inch, spaceAfter=0.2*inch))

    # Get section order from data, with fallback to default
    section_order = data.get('section_order', ['summary', 'experience', 'education', 'achievements', 'courses', 'skills', 'languages'])

    # Process sections in the specified order
    for section_key in section_order:
        if section_key == 'summary':
            if data.get('summary'):
                story.append(Paragraph("SUMMARY", styles['SectionTitle']))
                story.append(Paragraph(data['summary'], styles['NormalText']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'experience':
            experiences = data.get('experiences', [])
            if experiences:
                story.append(Paragraph("EXPERIENCE", styles['SectionTitle']))
                for exp in experiences:
                    if exp.get('title') and exp.get('company'):
                        story.append(Paragraph(exp['title'], styles['JobTitle']))
                        story.append(Paragraph(exp['company'], styles['CompanyInfo']))
                        
                        # Date and location line
                        date_location = []
                        if exp.get('start_date'):
                            date_str = exp['start_date']
                            if exp.get('end_date'):
                                date_str += f" - {exp['end_date']}"
                            elif exp.get('is_present'):
                                date_str += " - Present"
                            date_location.append(f"📅 {date_str}")
                        
                        if exp.get('location'):
                            date_location.append(f"📍 {exp['location']}")
                        
                        if date_location:
                            story.append(Paragraph(" | ".join(date_location), styles['DateLocation']))
                        
                        if exp.get('description'):
                            desc_lines = exp['description'].split('\n')
                            for line in desc_lines:
                                line = line.strip()
                                if line.startswith(('-', '*', '•')):
                                    story.append(Paragraph(f"• {line[1:].strip()}", styles['BulletPoint']))
                                elif line:
                                    story.append(Paragraph(line, styles['NormalText']))
                        story.append(Spacer(1, 0.15*inch))

        elif section_key == 'education':
            education_entries = data.get('education_entries', [])
            if education_entries:
                story.append(Paragraph("EDUCATION", styles['SectionTitle']))
                for edu in education_entries:
                    if edu.get('degree') and edu.get('institution'):
                        story.append(Paragraph(edu['degree'], styles['JobTitle']))
                        story.append(Paragraph(edu['institution'], styles['CompanyInfo']))
                        
                        # Date and location line
                        date_location = []
                        if edu.get('start_date'):
                            date_str = edu['start_date']
                            if edu.get('end_date'):
                                date_str += f" - {edu['end_date']}"
                            elif edu.get('is_present'):
                                date_str += " - Present"
                            date_location.append(f"📅 {date_str}")
                        
                        if edu.get('edu_location'):
                            date_location.append(f"📍 {edu['edu_location']}")
                        
                        if date_location:
                            story.append(Paragraph(" | ".join(date_location), styles['DateLocation']))
                        
                        if edu.get('edu_details'):
                            story.append(Paragraph(edu['edu_details'], styles['NormalText']))
                        story.append(Spacer(1, 0.1*inch))

        elif section_key == 'skills':
            if data.get('skills'):
                story.append(Paragraph("SKILLS", styles['SectionTitle']))
                
                # Create skills in a more organized layout
                skills_list = [skill.strip() for skill in data['skills'].split(',')]
                
                # Group skills into categories if possible, or just list them
                for skill in skills_list:
                    if skill:
                        story.append(Paragraph(skill, styles['SkillItem']))
                story.append(Spacer(1, 0.1*inch))

        elif section_key == 'achievements':
            key_achievements = data.get('key_achievements', [])
            if key_achievements:
                story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionTitle']))
                for achievement in key_achievements:
                    if achievement.get('title'):
                        story.append(Paragraph(f"🏆 {achievement['title']}", styles['JobTitle']))
                        if achievement.get('description'):
                            story.append(Paragraph(achievement['description'], styles['NormalText']))
                        story.append(Spacer(1, 0.05*inch))

        elif section_key == 'courses':
            courses = data.get('courses', [])
            if courses:
                story.append(Paragraph("CERTIFICATION", styles['SectionTitle']))
                for course in courses:
                    if course.get('title'):
                        story.append(Paragraph(course['title'], styles['CertificationTitle']))
                        if course.get('description'):
                            story.append(Paragraph(course['description'], styles['CertificationDesc']))

        elif section_key == 'languages':
            languages = data.get('languages', [])
            if languages:
                story.append(Paragraph("LANGUAGES", styles['SectionTitle']))
                
                # Create language table similar to the template
                lang_data = [["Language", "Level", "●●●●●"]]  # Header with dots representation
                
                for lang in languages:
                    if lang.get('name'):
                        level = lang.get('level', 'Conversational')
                        # Create dots based on level
                        dots = "●●●●●" if level == "Native" else "●●●●○" if level == "Advanced" else "●●●○○"
                        lang_data.append([lang['name'], level, dots])
                
                if len(lang_data) > 1:  # If we have languages beyond header
                    lang_table = Table(lang_data, colWidths=[1.5*inch, 1.5*inch, 1*inch])
                    lang_table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#F8F9FA')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#2C3E50')),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, -1), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#BDC3C7'))
                    ]))
                    story.append(lang_table)
                    story.append(Spacer(1, 0.1*inch))

    doc.build(story)
    buffer.seek(0)
    return buffer