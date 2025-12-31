import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/summarize"

st.set_page_config(page_title="Website Summarizer Agent", layout="wide")

st.title("🌐 Website Content Summarizer (LangGraph Agent)")

st.markdown("""
Paste any website URL below, and the LangGraph Agent will : 
1. Fetch the page  
2. Extract meaningful text  
3. Chunk it  
4. Summarize it  
""")

url = st.text_input("Enter Website URL:")

if st.button("Summarize"):
    if not url.strip():
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Summarizing..."):
            try:
                res = requests.post(API_URL, json={"url": url})
                data = res.json()

                if "error" in data:
                    st.error("❌ Error: " + data["error"])
                else:
                    st.success("Summary Generated Successfully!")
                    st.write(f"**Chunks Processed:** {data['num_chunks']}")

                    st.subheader("📌 Summary")
                    st.write(data["summary"])

            except Exception as e:
                st.error(f"Something went wrong: {e}")
