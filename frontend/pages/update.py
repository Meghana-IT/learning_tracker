import streamlit as st
import requests

st.title("Update Skill")

update_id = st.number_input(
    "Skill ID",
    step=1
)

new_skill_name = st.text_input("New Skill Name")

new_topics = st.text_area("New Topics")

new_level = st.selectbox("New Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

new_goal = st.text_area("New Goal")

new_date = st.date_input("New Completion Date")

if st.button("Update Skill"):

    payload = {

        "skill_name": new_skill_name,

        "topics": new_topics,

        "skill_level": new_level,

        "goal": new_goal,

        "completion_date": str(new_date)
    }

    response = requests.put(
        f"https://learning-tracker-ewhw.onrender.com/docs/update_skill/{update_id}",
        json=payload
    )

    st.success(response.json()["message"])

if st.button("⬅️ Back"):
    st.switch_page("pages/addskill.py")