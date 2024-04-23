import streamlit as st

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
	st.session_state.openai_api_key = ""

st.set_page_config(page_title="Home", page_icon="🦜️🔗")

# st.header("Welcome to LangChain! 👋")

st.markdown(
    """
    # DSCI 599 - Trends in Online Courses: A Data-Driven Analysis


    ## Introduction

    - To identify and analyze evolving trends in the design of courses and how these influence learner engagement on Coursera over the period from 2021 to 2024. The study aims to help educators and platforms optimize content to meet changing learner needs effectively.
    - Approach: Employing advanced machine learning techniques including Clustering Analysis and SHAP Analysis to analyze and predict key elements of successful course design.
    - Application:a personalized course recommendation system using Python and Streamlit.
	
    
    """
)


st.markdown(
    """
    ## Team Member
	Yuheng Chen, Haoyue Xu, Jingyue Zhang
    """
)