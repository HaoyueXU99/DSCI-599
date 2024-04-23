import streamlit as st

# # Initialize session state variables
# if 'openai_api_key' not in st.session_state:
# 	st.session_state.openai_api_key = "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"

st.set_page_config(page_title="Clustering", page_icon="🦜️🔗")

# st.header("Welcome to LangChain! 👋")

# st.markdown("![2024](./Clustering/2024.png)")

markdown_html =  """
    ## Clustering Analysis of Coursera Course Skills 
    > Deciphering Educational Patterns



    ### Dataset and Data Preprocessing
    - Data sourced from Kaggle for 2021, 2023, and 2024.
    - Datasets include course descriptions, skills, and ratings from Coursera.



    **Preprocessing: Text data tokenized, lemmatized, and cleansed of stopwords**



    ### Clustering model

    - Employed TF-IDF vectorization for feature extraction from skills data.
    - Used Truncated SVD to reduce dimensionality of TF-IDF vectors.
    - Applied KMeans clustering; number of clusters determined by silhouette scores.



    ----



    ### Clustering Results

    - 2021: Moderate cluster separation (Silhouette score: 0.524). Courses varied across disciplines.
    <img src="http://localhost:8000/Clustering/2021.png" width="600" style="display: block; margin-left: auto; margin-right: auto;">




    - 2023: Improved separation (Silhouette score: 0.618). Shift towards technical and professional skills.
    <img src="http://localhost:8000/Clustering/2023.png" width="600" style="display: block; margin-left: auto; margin-right: auto;">




    - 2024: Distinct clustering (Silhouette score: 0.778). Focus on advanced technology and project management.
    <img src="http://localhost:8000/Clustering/2024.png" width="600" style="display: block; margin-left: auto; margin-right: auto;">



    ---



    ### Analysis & Trends

    - Shift from broad academic topics like arts, social science to specialized technical skills reflects market demands.
    - Leadership and management appears in all three year. Enduring focus on management and leadership alongside technical training.
    - Online platforms rapidly adapting to technological advancements and job market needs. For instance, tensorflow become a popular skill.

    <img src="http://localhost:8000/Clustering/tables.png" width="700" style="display: block; margin-left: auto; margin-right: auto;">


    """

st.markdown(markdown_html, unsafe_allow_html=True)
