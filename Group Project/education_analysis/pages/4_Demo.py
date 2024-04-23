import os, streamlit as st
from openai import OpenAI
import pandas as pd
import ast
import re

st.set_page_config(page_title="Demo", page_icon="🦜️🔗")

file_path = "dataset/coursera_course_2024.csv"
df_2024 = pd.read_csv(file_path)
# json_data = df_2024.to_json(orient='records', lines=True)

# Get All skills
all_skills_text = ', '.join(df_2024['Skills'])
all_skills_list = all_skills_text.split(', ')

# Count the number of occurrences of each skill
skill_count = {}
for skill in all_skills_list:
    skill_count[skill] = skill_count.get(skill,0) + 1

# Sort the skills by their frequency
sorted_unique_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)

# Calculate the threshold for 90%
total_count = sum(skill_count.values())
threshold = total_count * 1

# Count the cumulative frequency
cumulative_count = 0
selected_skills = []
for skill, count in sorted_unique_skills:
    cumulative_count += count
    if cumulative_count <= threshold:
        selected_skills.append(skill)
    else:
        break


type_options = df_2024['Type'].unique()
difficulty_options = df_2024['Difficulty'].unique()



# Set API keys from session state
openai_api_key = st.session_state.openai_api_key

# Streamlit app
st.header(':female-teacher: Course Recommendation')



if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", 
                                     "content": "Hi.:wave: Please tell me what kind of courses you would like to study. \
                                        Let me know, and I will make recommendations for you." + "\n\n"
                                        "Also, please select the following options :point_down:"+ " \n"
                                        "- Choose the format that suits your learning style best from our options: {}.".format(", ".join(type_options)) + "\n"
                                        "- Select your preferred challenge level: {}.".format(", ".join(difficulty_options))}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


type_input = ""
difficulty_input = ""
skills_response = []
response_list = {}

if user_input := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    
    if len(skills_response) == 0:

        messages = []
        # prompt = f"Parses the following user requirements and returns matching skill names based on the provided skills list: \
        #                 \nUser requirements: \"{user_input}\"\nMatchable skills list: {selected_skills}\n\nPlease use matches the exact \
        #                 skill name in the list and returns at most 10 matching skills. Please give me only skill names separated by commas. "
        

        prompt = f"I want to extract key words from user input. Now, given the user input and a predefined list of skills, types, and difficulties, this script processes the user's requirements \
                            and matches them against available options. It ensures that the selected 'Skills', 'Type', and 'Difficulty' strictly adhere to the options listed in the input. \
                            The script then returns a dictionary showing the most relevant skills along with their associated difficulty and type.\n \
                            User input: \"{user_input}\"\n \
                            Available skills list: {selected_skills}\n \
                            Type list: {type_options}\n \
                            Difficulty list: {difficulty_options}\n \
                            Ensure that the output dictionary contains only items from these lists. The dictionary should be in this format:\n \
                            response_list = {{'Skills': 'Network Security, Python', 'Type': 'Course', 'Difficulty': 'Beginner'}} \
                            Remember, give me only the dictionary I need."

        
        messages.append({"role": "user", "content": prompt})



        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        
        response = client.chat.completions.create(model="gpt-3.5-turbo-0125", 
                                        messages=messages,
                                        max_tokens=255,
                                        temperature=0)



        msg = response.choices[0].message.content

    # st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)

    st.success(f"We extract your keywords successfully: {msg}")

    keywords_list = msg

    response_dict = {}
    match = re.search(r"\{.*?\}", keywords_list)
    
    if match:
        dict_str = match.group(0)
        # 将提取的字符串转换为字典
        response_dict = ast.literal_eval(dict_str)
    else:
        st.warn("Sorry, we couldn't find a dictionary in this response. Please try again.")

        

    print(response_dict)

    # 如果提取到了字典，并且字典不为空
    if response_dict:
        # 用字典中的键值对构建筛选条件
        query_conditions = []
        for key, value in response_dict.items():
            if key in df_2024.columns and key in ['Skills', 'Type', 'Difficulty']:  # 仅处理与CSV列匹配的关键字
                # 处理可能的多值匹配，如Skills列可能包含多个技能
                if key == 'Skills':
                    skills_query = ' | '.join(f"{key}.str.contains('{skill.strip()}')" for skill in value.split(','))
                    query_conditions.append(skills_query)
                else:
                    query_conditions.append(f"{key} == '{value}'")
        # 生成最终的查询语句并执行
        if query_conditions:
            query = ' & '.join(query_conditions)
            matching_courses = df_2024.query(query).sort_values('Review Count', ascending=False).head()


            markdown_text = "Here is what I found for you : \n\n"
            for index, row in matching_courses.iterrows():
                markdown_text += f"### :mortar_board: {row['Title']}\n\n"
                markdown_text += f"**Course Students Enrolled:** {row['course_students_enrolled']}  | **Review Count**: {row['Review Count']}  | **Ratings**: {row['Ratings']}\n\n"
                markdown_text += f"{row['course_description']}\n"
                markdown_text += "##### Skills\n"
                markdown_text += f"{row['Skills']}\n"
                markdown_text += "##### Difficulty\n"
                markdown_text += f"{row['Difficulty']}\n"
                markdown_text += "##### Type\n"
                markdown_text += f"{row['Type']}\n"
                markdown_text += "##### Duration\n"
                markdown_text += f"{row['Duration']}\n\n"
                markdown_text += f":point_right: [Click here to view the website.]({row['course_url']})\n\n"
                markdown_text += "--- \n\n"
                    
            # 显示符合条件的课程名称
            print(matching_courses['Title'])
            st.session_state.messages.append({"role": "assistant", "content": markdown_text})
            st.chat_message("assistant").write(markdown_text)
        else:
            print("No valid query could be constructed.")
    else:
        print("No dictionary found in the response or dictionary is empty.")
