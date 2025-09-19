import streamlit as st

st.set_page_config(page_title="AI Assistant")

st.title("Job Search :red[_AI Assistant_] :blue[:robot:]")

job_role = st.text_input(label=r"$\textsf{\Large Enter The Job Role You Are Interested}$",placeholder="eg. AI Engineer")

if job_role:
    st.write(f" You job role is {job_role} and now i am searching job roles related to {job_role}")
        