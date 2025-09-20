import streamlit as st

st.set_page_config(page_title="AI Assistant")

st.header("Job Search :red[_AI Assistant_] :blue[:robot:]")

if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""

def set_sidebar():
        with st.sidebar:
            st.subheader("API Configuration")
            gemini_api_key = st.text_input("Enter you Gemini API key:",type="password")
            
            if st.button("Done"):
                if gemini_api_key:
                    st.session_state.gemini_api_key = gemini_api_key
                    st.success("API Key Saved!")
                else:
                    st.warning("Please fill the gemini api key first")

def main():
    set_sidebar()
    if not st.session_state.gemini_api_key:
        st.warning("Please configure your API keys in the sidebar first")
        return
    job_role = st.text_input(label=r"$\textsf{\Large Enter The Job Role You Are Interested}$",placeholder="eg. AI Engineer")

    if job_role:
        st.write(f" You job role is {job_role} and now i am searching job roles related to {job_role}")
        
if __name__ == "__main__":
    main()