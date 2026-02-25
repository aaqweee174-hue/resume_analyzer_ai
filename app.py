import streamlit as st
from analyzer import analyze_resume
from invoice_generator import generate_invoice
from utils import extract_text

st.set_page_config(page_title="Resume Analyzer AI + Invoice Generator", layout="wide")
st.title("📄 Resume Analyzer AI + Invoice Generator")

# Sidebar for selecting feature
tabs = ["Resume Analyzer", "Invoice Generator"]
choice = st.sidebar.radio("Select Feature", tabs)

# ----- Resume Analyzer Tab -----
if choice == "Resume Analyzer":
    st.header("Resume Analyzer AI")
    
    uploaded_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description here")
    
    if st.button("Analyze Resume") and uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)
        ats, suggestions = analyze_resume(resume_text, job_desc)
        
        st.subheader("📊 ATS Score")
        st.progress(int(ats))
        st.write(f"{ats} / 100")
        
        st.subheader("💡 AI Suggestions")
        st.json(suggestions)

# ----- Invoice Generator Tab -----
elif choice == "Invoice Generator":
    st.header("Invoice Generator")

    items = []

    with st.form("invoice_form"):
        num_items = st.number_input("Number of Items", min_value=1, step=1)
        
        for i in range(num_items):
            col1, col2, col3 = st.columns(3)
            name = col1.text_input(f"Item {i+1} Name", key=f"name_{i}")
            qty = col2.number_input(f"Quantity", min_value=1, key=f"qty_{i}")
            price = col3.number_input(f"Price", min_value=0.0, key=f"price_{i}")
            items.append({"name": name, "qty": qty, "price": price})
        
        submitted = st.form_submit_button("Generate Invoice")

    if submitted:
        pdf_path = generate_invoice(items)
        st.success("Invoice generated!")
        
        # Download button outside the form
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="invoice.pdf")