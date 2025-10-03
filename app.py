import streamlit as st

st.set_page_config(page_title="AI Assistant")

st.header("Job Search :red[_AI Assistant_] :blue[:robot:]")

resume = st.file_uploader("Enter your resume in pdf format",type="pdf")

if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""
if 'custom_search_api_key' not in st.session_state:
    st.session_state.custom_search_api_key = ""
if 'custom_search_id' not in st.session_state:
    st.session_state.custom_search_id = ""

if resume:
    def set_sidebar():
        with st.sidebar:
            st.subheader("API Configuration")
            gemini_api_key = st.text_input("Enter you Gemini API key:",type="password")
            custom_search_api_key = st.text_input("Enter you Custom search API key:",type="password")
            custom_search_id = st.text_input("Enter you custom search ID:",type="password")



            if st.button("Done"):
                if gemini_api_key and custom_search_api_key and custom_search_id:
                    st.session_state.gemini_api_key = gemini_api_key
                    st.session_state.custom_search_api_key = custom_search_api_key
                    st.session_state.custom_search_id = custom_search_id

                    st.success("API Key Saved!")
                else:
                    st.warning("Please fill the api keys first")

    def main():
        set_sidebar()
        if not all([st.session_state.gemini_api_key,st.session_state.custom_search_api_key,st.session_state.custom_search_id]):
            st.warning("Please configure your API keys in the sidebar first")
            return
        st.write("Please choose one from job link or job search")
        link = st.button("Job Link")
        keyword = st.button("Job Search")

        if link:
            st.text_input("Paste job link")
        if keyword:
            st.text_input("Search job role with country",placeholder="example=Data scientist in india")

    if __name__ == "__main__":
            main()


