import streamlit as st
import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_BASE = os.getenv("API_BASE_URL")

st.set_page_config(page_title="Invoice HITL Review", layout="wide")
st.title("📄 Human-in-the-Loop Invoice Review")

# Upload invoice
st.header("Step 1: Upload an Invoice PDF")
uploaded_file = st.file_uploader("Choose a PDF invoice", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing invoice with OCR..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post(f"{API_BASE}/upload-invoice", files=files)

    if response.status_code == 200:
        extracted_text = response.json().get("text", "")
        st.success("OCR completed!")

        # Display raw OCR text
        st.subheader("Extracted Text")
        st.text_area("Raw OCR Output", value=extracted_text, height=300)

        st.header("Step 2: Validate / Correct Fields")
        vendor_name = st.text_input("Vendor Name")
        invoice_date = st.date_input("Invoice Date")
        total_amount = st.text_input("Total Amount")
        notes = st.text_area("Additional Notes", height=100)

        if st.button("✅ Submit Cleaned Data"):
            cleaned_data = {
                "vendor": vendor_name,
                "date": str(invoice_date),
                "total": total_amount,
                "notes": notes,
                "raw_text": extracted_text,
            }
            with st.spinner("Submitting cleaned data..."):
                response = requests.post(f"{API_BASE}/submit-cleaned", json=cleaned_data)
            
            if response.status_code == 200:
                st.success("✅ Invoice submitted successfully!")
            else:
                st.error(f"❌ Submission failed: {response.text}")
        else:
            st.error(f"OCR failed: {response.text}")