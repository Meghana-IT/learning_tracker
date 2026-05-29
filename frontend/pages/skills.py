import streamlit as st
import requests
import pandas as pd
st.title("Skills you mentioned")
st.write("Here you can view the skills you have added. Click on the skill name to see more details and make any necessary updates to your learning plan. Keep track of your progress and stay motivated on your learning journey!")

response = requests.get("http://localhost:8000/view_skills")

data=response.json()

df=pd.DataFrame(data,
columns=[
    "skill_id",
    "skill_name",
    "topics",
    "skill_level",
    "goal",
    "completion_date"


]
)
st.dataframe(df)

if st.button("🔙 Back"):

    st.switch_page("pages/addskill.py")
