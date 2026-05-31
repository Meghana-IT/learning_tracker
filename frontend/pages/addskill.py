import streamlit as st
import requests
st.title("Add skill")

with st.form("add_skill_form"):

    skill_name = st.text_input("Enter Skill Name")

    topics= st.text_area("Topics needed to learn")

    skill_level = st.selectbox("Skill Level", ["","Beginner", "Intermediate", "Advanced"])

    goal= st.text_area("Goal for learning this skill")

    completion_date = st.date_input("Expected Completion Date")

    submit_button = st.form_submit_button("Add Skill")

if submit_button:
    
    payload = {
        "skill_name": skill_name,
        "topics": topics,
        "skill_level": skill_level,
        "goal": goal,
        "completion_date": str(completion_date)
    }
    response = requests.post("https://learning-tracker-ewhw.onrender.com/docs/skills", json=payload)
    st.success(response.json()["message"])

col1,col2=st.columns(2)
with col1:
     if st.button("👀 View Skills"):
        st.switch_page("pages/skills.py")
    
with col2:
    if st.button("✏️ Update"):
        st.switch_page("pages/update.py")
