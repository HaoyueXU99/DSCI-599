import os, streamlit as st
from openai import OpenAI
import pandas as pd


file_path = "dataset/coursera_course_2024.csv"
df_2024 = pd.read_csv(file_path)
json_data = df_2024.to_json(orient='records', lines=True)

# Set API keys from session state
openai_api_key = st.session_state.openai_api_key

# Streamlit app
st.header('Course Recommendation')



if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Please tell me what kind of courses you would like to study. Let me know, and I will make recommendations for you."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)