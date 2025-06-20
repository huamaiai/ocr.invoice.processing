# tests/test_ocr_processor.py

import os
from backend.ocr.processor import process_invoice

def test_ocr_on_sample_invoice():
    sample_invoice_path = "data/sample_invoices/invoice_01.pdf"
    
    assert os.path.exists(sample_invoice_path), f"Sample file not found: {sample_invoice_path}"
    
    text = process_invoice(sample_invoice_path)
    
    print("----- OCR OUTPUT START -----")
    print(text[:1000])  # Print first 1000 chars
    print("----- OCR OUTPUT END -------")
    
    # Simple validation - adjust based on content of your sample invoice
    keywords = ["Invoice", "Total", "Date", "Amount"]
    for kw in keywords:
        assert kw.lower() in text.lower(), f"Missing expected keyword: {kw}"
