import streamlit as st
st.title("welcome to the learning tracker app")
st.write("This app is designed to help you track your learning progress and stay organized.You can log your learning activities,set goals, and monitor your growth over time. Whether you're learning a new skill, studying for an exam, or just want to keep track of your educational journey, this app has got you covered. Let's get started on your learning adventure!")
if st.button("Get Started"):
    st.switch_page("pages/addskill.py")
    