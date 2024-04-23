import streamlit as st

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
	st.session_state.openai_api_key = "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"

st.set_page_config(page_title="Course Recommendation", page_icon="🦜️🔗")

# st.header("Welcome to LangChain! 👋")

st.markdown(
    """

    ## Course Recommendation System for Coursera

    > Leveraging Cluster Analysis and SHAP for Enhanced Online Learning



    ### Course Recommendation System - Concept

    #### Goal
    Improve user experience through personalized course suggestions.

    #### Features
    Inputs for skills, course format, and difficulty.
    Personalized recommendations based on user preferences and data-driven insights.

    #### Data Preparation
    Use of "coursera_course_2024.csv" with comprehensive course details.

    #### Keyword Matching
    Employing GPT-3.5-turbo for effective input analysis.

    #### Course Filtering
    Dynamic query generation for tailored recommendations.

    #### User Interface
    Streamlit-based, easy-to-navigate application design.



    ---



    ### Challenges, Solutions and Future Enhancements

    #### Challenges
    - Complex keyword and metadata matching.
    - Balancing relevance and diversity in course recommendations.

    #### Solutions
    - Utilized NLP for improved keyword extraction and semantic matching.
    - Adjusted algorithm parameters to blend popular and niche offerings.

    #### Future Enhancements
    - **Data Needs**: More comprehensive user preference data to enable collaborative filtering.
    - **Recommendation Improvements**: Prioritize content aligned with detected trends for future recommendations.
    - **Objective**: Optimize user experience and expand user base.


    """
)
