import io
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Frame, PageTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, gray, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER # <--- THIS LINE IS CRUCIAL
from reportlab.lib.colors import HexColor, gray, white, black

# Define constants for layout
HEADER_HEIGHT = 1.5 * inch  # Height reserved for the header on the first page
COLUMN_GAP = 0.5 * inch     # Space between the two content columns

def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=0.75 * inch, leftMargin=0.75 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.75 * inch)

    styles = getSampleStyleSheet()

    # --- Custom Styles (as provided by user) ---
    styles.add(ParagraphStyle(name='NameHeader',
                              fontName='Helvetica-Bold',
                              fontSize=24,
                              leading=28,
                              alignment=TA_LEFT,
                              spaceAfter=0.1 * inch))

    styles.add(ParagraphStyle(name='ContactHeader',
                              fontName='Helvetica',
                              fontSize=10,
                              leading=12,
                              alignment=TA_LEFT,
                              spaceAfter=0.2 * inch))

    styles.add(ParagraphStyle(name='SectionTitle',
                              fontName='Helvetica-Bold',
                              fontSize=14,
                              leading=18,
                              spaceBefore=0.2 * inch,
                              spaceAfter=0.1 * inch,
                              textColor=HexColor('#333333')))

    styles.add(ParagraphStyle(name='JobTitle',
                              fontName='Helvetica-Bold',
                              fontSize=11,
                              leading=14))

    styles.add(ParagraphStyle(name='CompanyDate',
                              fontName='Helvetica-Oblique',
                              fontSize=10,
                              leading=12,
                              textColor=gray,
                              spaceAfter=0.05 * inch))

    styles.add(ParagraphStyle(name='BulletPoint',
                              parent=styles['Normal'],
                              leftIndent=0.25 * inch,
                              bulletIndent=0.1 * inch,
                              firstLineIndent=0,
                              spaceBefore=0.05 * inch))

    styles.add(ParagraphStyle(name='NormalIndented',
                              parent=styles['Normal'],
                              leftIndent=0.25 * inch))

    styles.add(ParagraphStyle(name='Justified',
                              parent=styles['Normal'],
                              alignment=TA_JUSTIFY))

    styles.add(ParagraphStyle(name='PersonalDetails',
                              parent=styles['Normal'],
                              alignment=TA_LEFT,
                              spaceAfter=0.05 * inch))

    # --- Header Content (these will be added to the story first) ---
    header_flowables = []
    if data.get('full_name'):
        header_flowables.append(Paragraph(data['full_name'].upper(), styles['NameHeader']))

    contact_info = []
    if data.get('email'): contact_info.append(data['email'])
    if data.get('phone'): contact_info.append(data['phone'])
    if data.get('linkedin'): contact_info.append(f"LinkedIn: {data['linkedin']}")
    if data.get('github'): contact_info.append(f"GitHub: {data['github']}")
    if data.get('website'): contact_info.append(f"Website: {data['website']}")
    if data.get('address'): contact_info.append(data['address'])

    if contact_info:
        header_flowables.append(Paragraph(" | ".join(contact_info), styles['ContactHeader']))

    header_flowables.append(HRFlowable(width="100%", thickness=0.5, color=gray, spaceBefore=0.1 * inch,
                                   spaceAfter=0.1 * inch))

    # --- Define Frames for Page Templates ---
    # Calculate common column width for two-column layout
    content_area_width = A4[0] - doc.leftMargin - doc.rightMargin
    col_width = (content_area_width - COLUMN_GAP) / 2

    # 1. Frames for the FIRST Page Layout
    # Header Frame (at the very top, covers the full content_area_width)
    frame_header_first_page = Frame(doc.leftMargin, A4[1] - doc.topMargin - HEADER_HEIGHT,
                                    content_area_width, HEADER_HEIGHT,
                                    id='header_frame', showBoundary=0) # showBoundary=1 for debugging frame outlines

    # Content Frames for the First Page (below the header)
    first_page_content_height = A4[1] - doc.topMargin - HEADER_HEIGHT - doc.bottomMargin
    frame_col1_first_page = Frame(doc.leftMargin, doc.bottomMargin, col_width, first_page_content_height,
                                  id='col1_first_page', showBoundary=0)
    frame_col2_first_page = Frame(doc.leftMargin + col_width + COLUMN_GAP, doc.bottomMargin, col_width, first_page_content_height,
                                  id='col2_first_page', showBoundary=0)

    # 2. Frames for LATER Pages (full height two columns)
    later_pages_content_height = A4[1] - doc.topMargin - doc.bottomMargin
    frame_col1_later_pages = Frame(doc.leftMargin, doc.bottomMargin, col_width, later_pages_content_height,
                                   id='col1_later_pages', showBoundary=0)
    frame_col2_later_pages = Frame(doc.leftMargin + col_width + COLUMN_GAP, doc.bottomMargin, col_width, later_pages_content_height,
                                   id='col2_later_pages', showBoundary=0)

    # --- Callback function for drawing the vertical column separator ---
    def draw_column_separator(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(gray)
        canvas.setLineWidth(0.5)

        line_x = A4[0] / 2 # X-coordinate for the line is always in the middle of the page

        # Determine the y-coordinates based on the current page number
        if canvas._pageNumber == 1:
            # First page: line goes from bottom margin up to the top of the content frames (below header)
            line_y_start = doc.bottomMargin
            line_y_end = A4[1] - doc.topMargin - HEADER_HEIGHT
        else:
            # Later pages: line goes from bottom margin up to the top margin (full content height)
            line_y_start = doc.bottomMargin
            line_y_end = A4[1] - doc.topMargin
        
        canvas.line(line_x, line_y_start, line_x, line_y_end)
        canvas.restoreState()

    # --- Page Templates ---
    # The first template contains the header frame, then the two body frames for page 1.
    first_page_template = PageTemplate(id='FirstPage', frames=[frame_header_first_page, frame_col1_first_page, frame_col2_first_page], onPage=draw_column_separator)
    # The later template contains only the two body frames, spanning the full page height.
    later_pages_template = PageTemplate(id='LaterPages', frames=[frame_col1_later_pages, frame_col2_later_pages], onPage=draw_column_separator)

    # Add both templates to the document. ReportLab will use the first one for page 1, then the second for subsequent pages.
    doc.addPageTemplates([first_page_template, later_pages_template])

    # --- Main Story Content (all sections *after* the header) ---
    # All content flowables are appended to a single list.
    # ReportLab's frame mechanism will automatically distribute them across columns and pages.
    main_body_story = []

    # Section Ordering (as provided by user)
    section_order = data.get('section_order', ['personal_details','summary', 'experience', 'education', 'skills', 'hobbies', 'languages', 'additional_info', 'references', 'projects','achievements','courses'])

    for section_key in section_order:

      if section_key == 'personal_details':
          personal_details_list = []
          if data.get('title_subtitle'):
              personal_details_list.append(f"<b>Job Title:</b> {data['title_subtitle']}")
          if data.get('location'):
              personal_details_list.append(f"<b>Location:</b> {data['location']}")
          if data.get('nationality'):
              personal_details_list.append(f"<b>Nationality:</b> {data['nationality']}")
          if data.get('birth_date'):
              personal_details_list.append(f"<b>Birth Date:</b> {data['birth_date']}")
          if data.get('gender'):
              personal_details_list.append(f"<b>Gender:</b> {data['gender']}")

          if personal_details_list:
              main_body_story.append(Paragraph("Personal Details", styles['SectionTitle']))
              for detail in personal_details_list:
                  main_body_story.append(Paragraph(detail, styles['PersonalDetails']))
              main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'summary':
          if data.get('summary'):
              main_body_story.append(Paragraph("Summary", styles['SectionTitle']))
              main_body_story.append(Paragraph(data['summary'], styles['Justified']))
              main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'experience':
          experiences = data.get('experiences', [])
          if experiences:
              main_body_story.append(Paragraph("Professional Experience", styles['SectionTitle']))
              for exp in experiences:
                  if exp.get('title') and exp.get('company'):
                      main_body_story.append(Paragraph(exp['title'], styles['JobTitle']))
                      main_body_story.append(Paragraph(f"{exp['company']} | {exp.get('start_date', 'N/A')} - {exp.get('end_date', 'Present')}", styles['CompanyDate']))
                      if exp.get('description'):
                          desc_lines = exp['description'].split('\n')
                          for line in desc_lines:
                              line = line.strip()
                              if line.startswith(('-', '*', '•')):
                                  main_body_story.append(Paragraph(line, styles['BulletPoint'], bulletText=line[0]))
                              elif line:
                                  main_body_story.append(Paragraph(line, styles['Justified']))
                      main_body_story.append(Spacer(1, 0.15 * inch))

      elif section_key == 'education':
          education_entries = data.get('education_entries', [])
          if education_entries:
              main_body_story.append(Paragraph("Education", styles['SectionTitle']))
              for edu in education_entries:
                  if edu.get('degree') and edu.get('institution'):
                      main_body_story.append(Paragraph(edu['degree'], styles['JobTitle']))
                      main_body_story.append(Paragraph(f"{edu['institution']} | {edu.get('start_date', 'N/A')} - {edu.get('end_date', 'Present')}", styles['CompanyDate']))
                      if edu.get('edu_details'):
                          main_body_story.append(Paragraph(edu['edu_details'], styles['Justified']))
                      main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'skills':
          if data.get('skills'):
              main_body_story.append(Paragraph("Skills", styles['SectionTitle']))
              main_body_story.append(Paragraph(data['skills'], styles['Justified']))
              main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'hobbies':
          if data.get('hobbies'):
              main_body_story.append(Paragraph("Hobbies", styles['SectionTitle']))
              main_body_story.append(Paragraph(data['hobbies'], styles['Justified']))
              main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'achievements':
          key_achievements = data.get('key_achievements', [])
          if key_achievements:
              main_body_story.append(Paragraph("Key Achievements", styles['SectionTitle']))
              for achievement in key_achievements:
                  if achievement.get('title'):
                      main_body_story.append(Paragraph(achievement['title'], styles['JobTitle']))
                      if achievement.get('description'):
                          main_body_story.append(Paragraph(achievement['description'], styles['NormalIndented']))
                      main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'courses':
          courses = data.get('courses', [])
          if courses:
              main_body_story.append(Paragraph("Courses", styles['SectionTitle']))
              for course in courses:
                  if course.get('title'):
                      main_body_story.append(Paragraph(course['title'], styles['JobTitle']))
                      if course.get('description'):
                          main_body_story.append(Paragraph(course['description'], styles['NormalIndented']))
                      main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'languages':
          languages = data.get('languages', [])
          if languages:
              main_body_story.append(Paragraph("Languages", styles['SectionTitle']))
              language_data = [["Language", "Reading", "Writing", "Conversation"]]  # Header
              for lang in languages:
                  language_data.append([
                      lang.get('name', ''),
                      lang.get('reading', 'N/A'),
                      lang.get('writing', 'N/A'),
                      lang.get('level', 'N/A')
                  ])

              language_table = Table(language_data)
              language_table.setStyle(TableStyle([
                  ('BACKGROUND', (0, 0), (-1, 0), HexColor("#333333")),
                  ('TEXTCOLOR', (0, 0), (-1, 0), white),
                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                  ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                  ('BACKGROUND', (0, 1), (-1, -1), white),
                  ('GRID', (0, 0), (-1, -1), 1, black)
              ]))
              main_body_story.append(language_table)
              main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'additional_info':
          additional_info = data.get('additional_info', [])
          if additional_info:
              main_body_story.append(Paragraph("Additional Info", styles['SectionTitle']))
              for info in additional_info:
                  if info.get('title'):
                      main_body_story.append(Paragraph(info['title'], styles['JobTitle']))
                      if info.get('description'):
                          main_body_story.append(Paragraph(info['description'], styles['NormalIndented']))
                      main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'references':
          references = data.get('references', [])
          if references:
              main_body_story.append(Paragraph("References", styles['SectionTitle']))
              for ref in references:
                  if ref.get('name'):
                      main_body_story.append(Paragraph(ref['name'], styles['JobTitle']))
                      main_body_story.append(Paragraph(f"{ref.get('title', 'N/A')}", styles['CompanyDate']))
                      if ref.get('phone'):
                          main_body_story.append(Paragraph(f"Phone: {ref['phone']}", styles['NormalIndented']))
                      if ref.get('description'):
                          main_body_story.append(Paragraph(ref['description'], styles['NormalIndented']))
                      main_body_story.append(Spacer(1, 0.1 * inch))

      elif section_key == 'projects':
          projects = data.get('projects', [])
          if projects:
              main_body_story.append(Paragraph("Projects", styles['SectionTitle']))
              for project in projects:
                  if project.get('title'):
                      main_body_story.append(Paragraph(project['title'], styles['JobTitle']))
                      if project.get('description'):
                          main_body_story.append(Paragraph(project['description'], styles['NormalIndented']))
                      if project.get('dates'):
                          main_body_story.append(Paragraph(f"Dates: {project['dates']}", styles['CompanyDate']))
                  main_body_story.append(Spacer(1, 0.1 * inch))

    # Combine header flowables with the main body story.
    # The header flowables will fill the header frame on the first page.
    # The remaining main_body_story will then flow into the two content columns.
    full_story = header_flowables + main_body_story

    doc.build(full_story)
    buffer.seek(0)
    return buffer

# Example usage (using the provided data, extended for multi-page testing)
data = {
    'full_name': 'Ellen Johnson',
    'title_subtitle': 'Marketing Manager',
    'location': 'Los Angeles, CA',
    'nationality': 'American',
    'birth_date': '1990-01-01',
    'gender': 'Female',
    'email': 'help@enhancv.com',
    'linkedin': 'linkedin.com/in/ellenjohnson',
    'github': 'github.com/ellenj',
    'website': 'ellenjohnson.com',
    'address': '123 Main St, Anytown, CA 90210',
    'summary': 'Motivated Digital Marketing Manager with over 3 years of experience in driving user acquisition and growth through strategic paid campaigns. Expert in data analysis, creative optimization, and cross-functional collaboration to achieve business objectives. Proven track record of scaling campaigns and enhancing ROI. This summary is extended to ensure it takes up significant space and potentially pushes content to the next column or page. It highlights a strong analytical mindset combined with practical application in digital marketing, emphasizing measurable results and leadership capabilities in a fast-paced environment. My goal is to leverage data-driven insights to maximize campaign performance and contribute to overall business growth. I am passionate about innovative marketing strategies and continuously seek opportunities to learn and adapt to new technologies and trends within the digital landscape. My proactive approach ensures campaigns are not only launched effectively but also continuously optimized for peak performance, delivering exceptional returns on investment for stakeholders.',
    'experiences': [
        {
            'title': 'Senior Digital Marketing Specialist',
            'company': 'Tech Innovate',
            'start_date': '01/2022',
            'end_date': 'Present',
            'description': '- Led the development and execution of comprehensive digital marketing campaigns across Meta, Google, and TikTok, increasing user acquisition by 45% within 12 months.\n- Managed a $500K quarterly budget for paid acquisition channels, optimizing spend for a 30% improvement in ROAS.\n- Implemented advanced targeting and retargeting strategies that reduced CPA by 20%, while increasing conversion rates by 15%.\n- Directed a team of junior specialists in campaign execution and performance monitoring, fostering a collaborative and results-driven environment. Achieved significant growth in key performance indicators by meticulously analyzing market trends and competitor strategies to refine campaign objectives.\n- Launched innovative experimental campaigns on emerging platforms, expanding reach and identifying new profitable customer segments, contributing to a 10% diversification of acquisition channels. Ensured compliance with all advertising policies and privacy regulations across all digital platforms, maintaining a high standard of ethical marketing practices. Collaborated extensively with product development and sales teams to align marketing initiatives with overall business goals, leading to cohesive and impactful campaigns. This extended description is to ensure the content flows well into multiple columns and potentially onto subsequent pages, testing the layout robustness.'
        },
        {
            'title': 'Junior Digital Marketing Specialist',
            'company': 'Growth Solutions',
            'start_date': '06/2020',
            'end_date': '12/2021',
            'description': '- Assisted in managing paid search and social campaigns, contributing to a 10% increase in lead generation.\n- Conducted A/B testing on ad creatives and landing pages, improving conversion rates by 5%.\n- Prepared weekly performance reports and presented insights to senior management.'
        },
        {
            'title': 'Marketing Intern',
            'company': 'Startup X',
            'start_date': '01/2020',
            'end_date': '05/2020',
            'description': '- Supported content marketing efforts, including blog post creation and social media scheduling.\n- Researched industry trends and competitor activities to inform strategy.'
        },
        {
            'title': 'Another Senior Digital Marketing Specialist Role',
            'company': 'Big Corp',
            'start_date': '01/2018',
            'end_date': '12/2019',
            'description': '- Oversaw a team of 3 marketing associates, ensuring campaign objectives were met.\n- Developed and launched new product marketing initiatives, resulting in a 25% market share increase.\n- Optimized marketing automation workflows, improving efficiency by 15%.'
        },
        {
            'title': 'Yet Another Digital Marketing Specialist',
            'company': 'Huge Corp',
            'start_date': '01/2016',
            'end_date': '12/2017',
            'description': '- Managed campaigns across various digital channels, including email and display advertising.\n- Collaborated with sales teams to align marketing efforts with sales goals.\n- Analyzed campaign data to identify opportunities for improvement and growth.'
        },
        {
            'title': 'Marketing Coordinator',
            'company': 'Small Biz',
            'start_date': '01/2014',
            'end_date': '12/2015',
            'description': '- Coordinated marketing events and webinars.\n- Managed company social media presence and engagement.\n- Assisted in creating marketing collateral.'
        }
    ],
    'education_entries': [
        {
            'degree': 'Master of Science in Marketing Analytics',
            'institution': 'University of California, Berkeley',
            'start_date': '01/2015',
            'end_date': '01/2017',
            'edu_details': 'Relevant coursework in strategic finance and operations management, including advanced statistical modeling, predictive analytics, and data visualization techniques. Completed a capstone project on customer lifetime value prediction using machine learning, which involved extensive data cleaning, model development, and validation.'
        },
        {
            'degree': 'Bachelor of Arts in Communication',
            'institution': 'University of Southern California',
            'start_date': '09/2010',
            'end_date': '05/2014',
            'edu_details': 'Graduated with honors. Focused on media studies and public relations, with a minor in digital media production. Participated in several student-led media projects and served as editor for the university\'s communication journal for two semesters, gaining valuable experience in content creation and editorial processes.'
        }
    ],
    'skills': 'Data Analysis, Paid Acquisition, Retargeting, ROAS Optimization, Cross-Functional Collaboration, Google Analytics, Looker, Appsflyer, Meta Advertising, Google Ads, TikTok Ads, Snapchat Ads, SQL, Python for Data Analysis, Tableau, Power BI, Content Marketing, SEO, SEM, Email Marketing, Social Media Marketing, Project Management, CRM Software, Salesforce, HubSpot, Market Research, Competitor Analysis, Strategic Planning, Budget Management, Public Speaking, Team Leadership, Mentoring, Problem Solving, Critical Thinking, Adaptability, Creativity, Innovation, Customer Relationship Management, Client Communication, Negotiation, Presentation Skills, Microsoft Office Suite, Google Workspace, Adobe Creative Suite (Basic), Web Analytics, A/B Testing, User Experience (UX) Principles, Conversion Rate Optimization (CRO), Brand Management, Product Launch, International Marketing, E-commerce, Mobile Marketing, Video Marketing, Influencer Marketing, Partnership Development, Campaign Management, Performance Marketing, Digital Strategy, Growth Hacking, Storytelling, Copywriting, Marketing Automation, Lead Nurturing, Customer Journey Mapping, Data Storytelling, Demand Generation, Account-Based Marketing (ABM), Customer Success, Performance Reporting.',
    'hobbies': 'Reading, Hiking, Photography, Cooking, Cycling, Traveling, Volunteering, Playing Musical Instruments, Learning New Languages, Writing, Painting, Yoga, Meditation, Gaming, Sports, Gardening, Watching Documentaries, Attending Workshops, Exploring New Cuisines, Running, Swimming, Board Games, Puzzles, Coding Personal Projects, Astronomy, Bird Watching, Collecting Stamps, Calligraphy, Dancing, Debating, Drawing, Embroidery, Fishing, Genealogy, Golf, Horse Riding, Jewelry Making, Jigsaw Puzzles, Juggling, Knitting, Magic, Martial Arts, Origami, Parkour, Philosophy, Podcasting, Pottery, Quilting, Robotics, Rock Climbing, Roller Skating, Sculpting, Singing, Skating, Skydiving, Snowboarding, Stand-up Comedy, Surfing, Table Tennis, Tai Chi, Tennis, Theatre, Urban Exploration, Video Editing, Watching Movies, Weightlifting, Woodworking, Writing Poetry.',
    'languages': [
        {'name': 'English', 'reading': 'Fluent', 'writing': 'Advanced', 'level': 'Fluent'},
        {'name': 'Spanish', 'reading': 'Intermediate', 'writing': 'Basic', 'level': 'Conversational'},
        {'name': 'French', 'reading': 'Basic', 'writing': 'Basic', 'level': 'Basic'},
        {'name': 'German', 'reading': 'N/A', 'writing': 'N/A', 'level': 'Beginner'}
    ],
    'key_achievements': [
            {'title': 'Increased Sales by 20%', 'description': 'Successfully increased sales figures by 20% within the first quarter by implementing a new sales strategy and training team members on advanced negotiation techniques. This led to a significant boost in revenue for the company, contributing directly to quarterly financial targets. Demonstrated strong leadership in motivating the sales force and optimizing sales processes.'},
            {'title': 'Improved Customer Satisfaction', 'description': 'Enhanced customer satisfaction through strategic service improvements, including the rollout of a 24/7 customer support chatbot and a revamped feedback collection system. Customer satisfaction scores rose by 15%, leading to increased customer retention and positive brand perception. This initiative involved cross-departmental collaboration and meticulous planning.'},
            {'title': 'Reduced Operational Costs', 'description': 'Implemented cost-saving measures that significantly reduced operational expenses by 10% annually without compromising service quality. This was achieved through vendor renegotiations, process automation, and optimization of resource allocation. The savings were redirected to high-impact growth initiatives.'},
            {'title': 'Launched New Product Line', 'description': 'Successfully led the cross-functional team in launching a new product line from concept to market, exceeding initial sales targets by 30% in the first six months. This involved comprehensive market research, agile product development methodologies, and a robust, multi-channel marketing campaign. The project showcased strong project management and strategic marketing skills.'}
        ],
    'courses': [
            {'title': 'Marketing Strategy Certification', 'description': 'Advanced marketing strategy course by renowned industry experts, covering digital marketing, brand management, and market analysis. Completed with distinction, demonstrating a deep understanding of strategic planning and execution in diverse market environments.'},
            {'title': 'Financial Analysis for Non-Financial Managers', 'description': 'Comprehensive course on financial analysis and investment strategies, focusing on budgeting, forecasting, and financial reporting. Gained a deeper understanding of business finance, enabling better decision-making in marketing budget allocation and ROI analysis.'},
            {'title': 'Project Management Professional (PMP) Prep', 'description': 'Intensive training course for the PMP certification, covering all aspects of project initiation, planning, execution, monitoring, control, and closing. Acquired best practices in project management, improving efficiency and successful project delivery.'}
        ],
    'additional_info': [
        {'title': 'Volunteering Experience', 'description': 'Active volunteer at a local animal shelter, assisting with animal care and adoption events since 2021. Dedicate 4-6 hours per week to supporting animal welfare and community engagement. This experience has honed my organizational and empathetic communication skills.'},
        {'title': 'Awards and Recognition', 'description': 'Recipient of the "Employee of the Year" award in 2023 for outstanding contributions to digital marketing campaigns, specifically for the Q3 campaign that achieved a 45% increase in user acquisition. Also recognized with the "Innovation Award" in 2022 for leading a successful experimental marketing initiative.'},
        {'title': 'Publications', 'description': 'Authored an article on "The Future of AI in Marketing" published in Digital Marketing Magazine in 2022. This article explored the implications of artificial intelligence on personalized marketing strategies and predicted upcoming trends in the industry, receiving positive feedback from peers and industry experts. Currently working on a follow-up article exploring the ethical considerations of AI in consumer data analysis.'}
    ],
    'references': [
        {'name': 'John Doe', 'title': 'Former Manager at Tech Innovate', 'phone': '555-123-4567', 'description': 'Excellent professional, highly recommended. John consistently exceeded expectations and was a key contributor to our team\'s success in driving digital marketing initiatives.'},
        {'name': 'Jane Smith', 'title': 'Colleague at Growth Solutions', 'phone': '555-987-6543', 'description': 'Great team player and very dedicated. Jane\'s collaborative spirit and analytical skills were instrumental in achieving our campaign goals and improving overall team performance.'}
    ],
    'projects': [
        {'title': 'E-commerce Platform Redesign', 'description': 'Led the marketing efforts for a complete redesign of the company\'s e-commerce platform, focusing on user experience and conversion rate optimization, resulting in a 25% increase in conversion rates. This involved A/B testing, user feedback analysis, and collaboration with UX/UI designers.', 'dates': 'Jan 2023 - Jun 2023'},
        {'title': 'Mobile App User Acquisition Campaign', 'description': 'Developed and executed a successful user acquisition campaign for a new mobile app across various channels (Meta, Google, Apple Search Ads), driving over 100,000 downloads in the first month with a CPA 15% below target. Utilized advanced targeting and optimization techniques.', 'dates': 'Aug 2022 - Nov 2022'},
        {'title': 'Content Strategy for SaaS Startup', 'description': 'Designed and implemented a comprehensive content strategy for a new SaaS startup, improving organic search visibility by 50% within six months. This project involved extensive keyword research, content calendar planning, SEO optimization for all published articles and landing pages, and content distribution across various social media channels to maximize reach and engagement. The efforts resulted in a significant increase in inbound leads and brand authority in the competitive SaaS market, demonstrating strong analytical and strategic skills in content development and execution. This project also involved setting up a robust content performance tracking system using Google Analytics and Looker Studio.', 'dates': 'Mar 2022 - Present'},
    ],
    'section_order': ['personal_details', 'summary', 'experience', 'education', 'skills', 'projects', 'achievements', 'courses', 'languages', 'additional_info', 'hobbies', 'references']
}


pdf_buffer = generate_pdf(data)

# Save the PDF to a file
with open('resume_multipage_two_column_fixed.pdf', 'wb') as f:
    f.write(pdf_buffer.read())