import streamlit as st

st.title("AI Resume Screening System")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes", accept_multiple_files=True
)

if st.button("Screen"):
    st.write("Processing...")
    