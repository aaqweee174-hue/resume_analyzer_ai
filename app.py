import streamlit as st
import sys
import os

# 🔥 FIX: Add project root to Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils import extract_text
from analyzer import analyze_resume

# Page config
st.set_page_config(page_title="Resume Analyzer AI", page_icon="📄")

# Title
st.title("📄 Resume Analyzer AI")
st.write("Upload your resume and get ATS score + AI suggestions")

# File upload
uploaded_file = st.file_uploader("Upload your CV (PDF only)", type=["pdf"])

# Job description
job_desc = st.text_area("Paste Job Description here")

# Analyze button
if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("⚠️ Please upload your CV")
    
    elif not job_desc.strip():
        st.warning("⚠️ Please enter job description")

    else:
        try:
            with st.spinner("Analyzing resume... ⏳"):
                
                # Extract text
                resume_text = extract_text(uploaded_file)

                if not resume_text.strip():
                    st.error("❌ Could not read PDF properly")
                else:
                    # Analyze
                    ats_score, suggestions = analyze_resume(resume_text, job_desc)

                    # Show ATS score
                    st.subheader("📊 ATS Score")
                    st.success(f"{ats_score} / 100")

                    # Progress bar
                    st.progress(int(ats_score))

                    # Suggestions
                    st.subheader("💡 AI Suggestions")
                    st.write(suggestions)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("🚀 Built by Yousaf | Resume Analyzer AI")