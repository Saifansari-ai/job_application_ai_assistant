import streamlit as st

st.set_page_config(page_title="AI Assistant")

st.title("Job Search :red[_AI Assistant_] :blue[:robot:]")

st.markdown("""
    <style>
    .stTextInput > label {
        font-size: 120%; /* Adjust this value as needed */
        font-weight: bold; /* Optional: make the label bold */
    }
    </style>
""", unsafe_allow_html=True)

job_role = st.text_input(label=r"$\textsf{\Large Enter The Job Role You Are Interested}$",placeholder="eg. AI Engineer")

if job_role:
    st.write(f" You job role is {job_role} and now i am searching job roles related to {job_role}")
        