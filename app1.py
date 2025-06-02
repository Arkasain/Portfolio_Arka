import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Arka Sain - Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    .skill-badge {
        display: inline-block;
        background: linear-gradient(45deg, #1f77b4, #17a2b8);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .experience-card {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
    }
    .achievement-badge {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #333;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        display: inline-block;
        margin: 0.3rem;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "👨‍💼 About", "🛠️ Skills", "💼 Experience", "🚀 Projects", "🏆 Achievements", "📜 Certifications",
     "📞 Contact"]
)


# Helper function to create skill badges
def create_skill_badges(skills_list):
    badges_html = ""
    for skill in skills_list:
        badges_html += f'<span class="skill-badge">{skill}</span>'
    return badges_html


# HOME PAGE
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Arka Sain</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Data Analyst | Business Analytics Enthusiast | Machine Learning Practitioner</p>',
        unsafe_allow_html=True)

    # Hero section with metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f77b4; margin: 0;">📊</h3>
            <h4 style="margin: 0.5rem 0;">Data Analysis</h4>
            <p style="margin: 0; color: #666;">Expert Level</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f77b4; margin: 0;">🎓</h3>
            <h4 style="margin: 0.5rem 0;">Education</h4>
            <p style="margin: 0; color: #666;">PGP + MBA</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f77b4; margin: 0;">🏆</h3>
            <h4 style="margin: 0.5rem 0;">Projects</h4>
            <p style="margin: 0; color: #666;">5+ Completed</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f77b4; margin: 0;">📜</h3>
            <h4 style="margin: 0.5rem 0;">Certifications</h4>
            <p style="margin: 0; color: #666;">5+ Earned</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick overview
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h2 class="section-header">👋 Welcome to My Portfolio</h2>', unsafe_allow_html=True)
        st.markdown("""
        I'm a passionate **Data Analyst** and **Business Analytics** student with hands-on experience in:

        - **Data Analysis & Visualization** using Power BI, Tableau, and Python
        - **Machine Learning** implementations with real-world datasets
        - **Business Intelligence** dashboard development
        - **Statistical Analysis** and predictive modeling

        Currently pursuing **PGP + MBA in Business Analytics & Data Science** at Bengal Institute of Business Studies, 
        I combine technical expertise with business acumen to derive actionable insights from data.
        """)

    with col2:
        st.markdown("""
        <div class="contact-info">
            <h3>📞 Quick Contact</h3>
            <p><strong>📱 Phone:</strong> +91 7410173864</p>
            <p><strong>📧 Email:</strong> sainarka2@gmail.com</p>
            <p><strong>📍 Location:</strong> Kolkata, West Bengal</p>
        </div>
        """, unsafe_allow_html=True)

# ABOUT PAGE
elif page == "👨‍💼 About":
    st.markdown('<h1 class="section-header">About Me</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### 🎯 Professional Summary

        I'm a dedicated **Data Analyst** with a strong foundation in **Business Analytics** and **Data Science**. 
        My journey in data analytics began during my BCA studies and has evolved through practical internships 
        and diverse project experiences.

        ### 🌟 What Drives Me

        - **Problem-Solving**: I love transforming complex data into actionable business insights
        - **Continuous Learning**: Always exploring new tools and techniques in data science
        - **Business Impact**: Focused on creating solutions that drive real business value
        - **Collaboration**: Enjoy working in teams to achieve common goals

        ### 🎯 Career Objective

        To leverage my analytical skills and business acumen in a challenging data analyst role where I can 
        contribute to data-driven decision making and help organizations unlock the power of their data.
        """)

    with col2:
        st.markdown("""
        ### 📚 Educational Journey

        **🎓 Current (2024-Present)**  
        **PGP + MBA** - Business Analytics & Data Science  
        *Bengal Institute of Business Studies*  
        **Grade:** 77%

        **🎓 2021-2024**  
        **BCA (Hons)**  
        *Burdwan Institute of Management and Computer Science*  
        **Grade:** 71%

        **🎓 2021**  
        **WBCHSE - Science**  
        *Raina Swami Bholananda Vidyayatan School*  
        **Grade:** 71%

        ### 🎲 Personal Interests
        - 🏆 Sports (College Champion)
        - 📊 Data Visualization
        - 🤖 Machine Learning Research
        - 📱 Technology Trends
        """)

# SKILLS PAGE
elif page == "🛠️ Skills":
    st.markdown('<h1 class="section-header">Technical Skills</h1>', unsafe_allow_html=True)

    # Programming Languages
    st.markdown("### 💻 Programming Languages")
    languages = ["Python", "SQL", "HTML", "C"]
    st.markdown(create_skill_badges(languages), unsafe_allow_html=True)

    # Create a skills proficiency chart
    skills_data = {
        'Skill': ['Python', 'SQL', 'Power BI', 'Excel', 'Tableau', 'Pandas', 'Machine Learning'],
        'Proficiency': [90, 85, 95, 90, 80, 88, 75]
    }

    fig = px.bar(
        skills_data,
        x='Proficiency',
        y='Skill',
        orientation='h',
        title='Technical Skills Proficiency',
        color='Proficiency',
        color_continuous_scale='Blues'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🛠️ Technologies & Tools")
        tech_tools = ["Power BI", "Tableau", "Advanced Excel", "MySQL", "Pandas", "NumPy", "Seaborn", "Matplotlib",
                      "Scikit-Learn", "Jupyter", "PyCharm"]
        st.markdown(create_skill_badges(tech_tools), unsafe_allow_html=True)

    with col2:
        st.markdown("### 🧠 Core Competencies")
        core_skills = ["Data Analysis", "Data Visualization", "Critical Thinking", "Communication", "Leadership",
                       "Statistical Analysis", "Business Intelligence"]
        st.markdown(create_skill_badges(core_skills), unsafe_allow_html=True)

    # Skills radar chart
    st.markdown("### 📊 Skills Overview")

    categories = ['Programming', 'Data Analysis', 'Visualization', 'Machine Learning', 'Business Intelligence',
                  'Communication']
    values = [85, 90, 95, 75, 88, 82]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Level',
        line=dict(color='#1f77b4')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Skills Radar Chart"
    )

    st.plotly_chart(fig, use_container_width=True)

# EXPERIENCE PAGE
elif page == "💼 Experience":
    st.markdown('<h1 class="section-header">Professional Experience</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="experience-card">
        <h3>🔍 Data Analyst Intern</h3>
        <h4>PRODIGY INFOTECH - Tech Services</h4>
        <p><strong>📅 Duration:</strong> April 2025 – May 2025</p>
        <p><strong>📍 Location:</strong> Kolkata, West Bengal, India</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Key Responsibilities & Achievements")

    experience_data = [
        {
            "Task": "Data Visualization",
            "Description": "Created visualizations (bar charts, histograms) to analyze and represent distributions of categorical and continuous variables in population datasets",
            "Skills": ["Power BI", "Python", "Data Visualization"]
        },
        {
            "Task": "Exploratory Data Analysis",
            "Description": "Performed end-to-end data cleaning and EDA using real-world datasets such as the Titanic dataset to uncover trends, patterns, and relationships",
            "Skills": ["Pandas", "Python", "Data Cleaning"]
        },
        {
            "Task": "Machine Learning",
            "Description": "Built and trained a decision tree classifier using the Bank Marketing dataset from UCI to predict customer behavior",
            "Skills": ["Scikit-Learn", "Machine Learning", "Classification"]
        },
        {
            "Task": "Sentiment Analysis",
            "Description": "Conducted sentiment analysis on social media datasets to identify and visualize public opinion trends and attitudes toward various brands",
            "Skills": ["NLP", "Python", "Social Media Analytics"]
        },
        {
            "Task": "Traffic Analysis",
            "Description": "Analyzed traffic accident datasets to discover key patterns associated with road conditions, weather, and time of day",
            "Skills": ["Statistical Analysis", "Pattern Recognition", "Data Mining"]
        }
    ]

    for i, exp in enumerate(experience_data):
        with st.expander(f"📋 {exp['Task']}", expanded=True):
            st.write(exp['Description'])
            st.markdown("**Skills Used:**")
            st.markdown(create_skill_badges(exp['Skills']), unsafe_allow_html=True)

    # Experience timeline
    st.markdown("### 📅 Career Timeline")

    timeline_data = pd.DataFrame({
        'Year': [2021, 2021, 2024, 2024, 2025, 2025],
        'Event': ['Started BCA', 'WBCHSE Graduation', 'BCA Graduation', 'Started PGP+MBA', 'Data Analyst Internship',
                  'Present']
    })

    fig = px.line(timeline_data, x='Year', y='Event', title='Career Timeline', markers=True)
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# PROJECTS PAGE
elif page == "🚀 Projects":
    st.markdown('<h1 class="section-header">Featured Projects</h1>', unsafe_allow_html=True)

    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>📊 Sales & Business Insights Dashboard</h3>
        <p><strong>Technology:</strong> Power BI</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Project Overview:**
        Designed and developed a comprehensive Sales & Business Insights Dashboard in Power BI to visualize 
        key performance indicators (KPIs), sales trends, and regional insights for improved business decision-making.

        **Key Features:**
        - Dynamic reports with interactive visuals
        - DAX measures for complex calculations
        - Slicers and filters for user interaction
        - Regional performance analysis
        - Sales trend identification
        """)

    with col2:
        st.markdown("""
        **Technologies Used:**
        """)
        project1_skills = ["Power BI", "DAX", "Data Cleaning", "EDA", "KPI Development"]
        st.markdown(create_skill_badges(project1_skills), unsafe_allow_html=True)

    st.markdown("---")

    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>🛒 Blink IT Sales Power BI Dashboard</h3>
        <p><strong>Technology:</strong> Power BI, Advanced Analytics</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Project Overview:**
        Comprehensive analysis of 12+ months of sales data to uncover key business insights and performance drivers.

        **Key Achievements:**
        - Analyzed over 12 months of sales data
        - Identified top-performing products and underperforming regions
        - Discovered that 60% of total revenue came from 3 key products
        - Created dynamic visuals and KPIs for monitoring targets
        - Enabled data-driven sales strategies and quarterly reviews
        """)

    with col2:
        st.markdown("""
        **Impact Metrics:**
        """)

        # Create impact metrics visualization
        impact_data = {
            'Metric': ['Revenue Analysis', 'Product Performance', 'Regional Insights', 'Decision Support'],
            'Impact': [95, 90, 85, 92]
        }

        fig = px.bar(impact_data, x='Impact', y='Metric', orientation='h',
                     title='Project Impact Metrics', color='Impact',
                     color_continuous_scale='Greens')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

    # Additional Projects Section
    st.markdown("### 🛠️ Technical Projects from Internship")

    projects = [
        {
            "title": "🧠 Decision Tree Classifier",
            "description": "Built and trained a decision tree classifier using UCI Bank Marketing dataset",
            "dataset": "Bank Marketing Dataset (UCI)",
            "outcome": "Customer behavior prediction model"
        },
        {
            "title": "😊 Sentiment Analysis Engine",
            "description": "Social media sentiment analysis for brand perception tracking",
            "dataset": "Social Media Datasets",
            "outcome": "Public opinion trend visualization"
        },
        {
            "title": "🚗 Traffic Accident Analysis",
            "description": "Pattern analysis of traffic accidents with weather and time correlations",
            "dataset": "Traffic Accident Datasets",
            "outcome": "Accident hotspot identification"
        }
    ]

    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i]:
            st.markdown(f"""
            <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; height: 200px;">
                <h4>{project['title']}</h4>
                <p><strong>Dataset:</strong> {project['dataset']}</p>
                <p>{project['description']}</p>
                <p><strong>Outcome:</strong> {project['outcome']}</p>
            </div>
            """, unsafe_allow_html=True)

# ACHIEVEMENTS PAGE
elif page == "🏆 Achievements":
    st.markdown('<h1 class="section-header">Achievements & Recognition</h1>', unsafe_allow_html=True)

    achievements = [
        {
            "title": "🏆 College Sport Champion - BIBS",
            "date": "March 2025",
            "description": "Recognized for outstanding performance in college sports competitions",
            "category": "Sports"
        },
        {
            "title": "🥇 Top 5 Finalist in IBM Technovate - BIBS",
            "date": "April 2025",
            "description": "Selected among top 5 finalists in IBM's technology innovation competition",
            "category": "Technology"
        },
        {
            "title": "🎉 Team Day and Theme Day - BIBS",
            "date": "April 2024",
            "description": "Active participation and recognition in college team building activities",
            "category": "Leadership"
        }
    ]

    for achievement in achievements:
        st.markdown(f"""
        <div class="achievement-badge">
            <h3>{achievement['title']}</h3>
            <p><strong>📅 Date:</strong> {achievement['date']}</p>
            <p><strong>📋 Category:</strong> {achievement['category']}</p>
            <p>{achievement['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Achievement categories visualization
    category_data = pd.DataFrame({
        'Category': ['Sports', 'Technology', 'Leadership'],
        'Count': [1, 1, 1]
    })

    fig = px.pie(category_data, values='Count', names='Category',
                 title='Achievement Categories Distribution',
                 color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    st.plotly_chart(fig, use_container_width=True)

# CERTIFICATIONS PAGE
elif page == "📜 Certifications":
    st.markdown('<h1 class="section-header">Professional Certifications</h1>', unsafe_allow_html=True)

    certifications = [
        {
            "title": "🤖 Machine Learning with Python",
            "issuer": "IIT Kanpur",
            "description": "Foundational machine learning concepts using Python",
            "skills": ["Python", "Machine Learning", "Algorithms"]
        },
        {
            "title": "💼 Data Science Job Simulation",
            "issuer": "Forage",
            "description": "Practical data science project simulation",
            "skills": ["Data Science", "Project Management", "Real-world Applications"]
        },
        {
            "title": "🐍 Python 101 for Data Science",
            "issuer": "IBM Developer Skills Network",
            "description": "Data Science techniques and tools using Python",
            "skills": ["Python", "Data Science", "Programming"]
        },
        {
            "title": "🗄️ SQL & Relational Databases 101",
            "issuer": "IBM",
            "description": "SQL skills for database management and querying",
            "skills": ["SQL", "Database Management", "Data Querying"]
        },
        {
            "title": "📊 Advanced Excel with Power BI",
            "issuer": "BIBS",
            "description": "Advanced Excel & Power BI for Data Analysis, Visualization, and Reporting",
            "skills": ["Excel", "Power BI", "Data Analysis", "Reporting"]
        }
    ]

    for cert in certifications:
        with st.expander(f"📜 {cert['title']}", expanded=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**Issuer:** {cert['issuer']}")
                st.markdown(f"**Description:** {cert['description']}")
                st.markdown("**Skills Gained:**")
                st.markdown(create_skill_badges(cert['skills']), unsafe_allow_html=True)

            with col2:
                st.markdown("### 🎯 Status")
                st.success("✅ Completed")

    # Certification timeline
    st.markdown("### 📅 Certification Timeline")

    cert_timeline = pd.DataFrame({
        'Certification': ['Python 101', 'SQL & Databases', 'Advanced Excel', 'ML with Python',
                          'Data Science Simulation'],
        'Year': [2024, 2024, 2024, 2025, 2025],
        'Importance': [8, 9, 8, 10, 9]
    })

    fig = px.scatter(cert_timeline, x='Year', y='Certification', size='Importance',
                     title='Certification Journey', color='Importance',
                     color_continuous_scale='Viridis')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# CONTACT PAGE
elif page == "📞 Contact":
    st.markdown('<h1 class="section-header">Get In Touch</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### 📬 Let's Connect!

        I'm always interested in new opportunities, collaborations, and interesting projects. 
        Whether you're looking for a data analyst, have a project in mind, or just want to 
        chat about data science, feel free to reach out!

        ### 🎯 What I'm Looking For:
        - **Full-time Data Analyst positions**
        - **Freelance data analysis projects**
        - **Collaboration opportunities**
        - **Mentorship in advanced analytics**
        """)

        # Contact form
        st.markdown("### 📝 Send me a message:")

        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject",
                                   ["Job Opportunity", "Project Collaboration", "General Inquiry", "Other"])
            message = st.text_area("Message", height=100)

            submitted = st.form_submit_button("Send Message")

            if submitted:
                st.success("Thank you for your message! I'll get back to you soon. 📧")
                st.balloons()

    with col2:
        st.markdown("""
        <div class="contact-info">
            <h3>📞 Contact Information</h3>
            <p><strong>📱 Phone:</strong><br>+91 7410173864</p>
            <p><strong>📧 Email:</strong><br>sainarka2@gmail.com</p>
            <p><strong>📍 Location:</strong><br>Kolkata, West Bengal, India</p>
            <p><strong>🔗 LinkedIn:</strong><br>Connect with me</p>
            <p><strong>💻 GitHub:</strong><br>View my code</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🌍 Find Me Online")

        # Social media links (placeholder buttons)
        if st.button("🔗 LinkedIn Profile"):
            st.info("LinkedIn profile link would open here")

        if st.button("💻 GitHub Repository"):
            st.info("GitHub profile link would open here")

        if st.button("📧 Send Email"):
            st.info("Email client would open here")

        # Quick stats
        st.markdown("### 📊 Quick Stats")

        stats_data = {
            'Metric': ['Projects Completed', 'Certifications', 'Years of Study', 'Programming Languages'],
            'Value': [5, 5, 3, 4]
        }

        for i, (metric, value) in enumerate(zip(stats_data['Metric'], stats_data['Value'])):
            st.metric(label=metric, value=value)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🚀 Built with Streamlit | 📊 Powered by Data | ❤️ Made by Arka Sain</p>
    <p>© 2025 Arka Sain. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
