# FastAPI app entrypoint

# backend/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from backend.ocr.processor import process_invoice
from backend.schemas import CleanedInvoice
from backend.db.mysql_dao import insert_invoice_mysql
from backend.db.mongo_dao import insert_invoice_mongo
from backend.logger import logger
import tempfile
import shutil

app = FastAPI(title="Invoice Processing API")

@app.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        extracted_text = process_invoice(tmp_path)
        return JSONResponse(content={"text": extracted_text[:2000]})  # Truncate for demo

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/invoice-log")
async def get_invoice_log():
    # Placeholder for future DB query
    return {"message": "Logs will appear here."}

@app.post("/submit-cleaned")
async def submit_cleaned_invoice(invoice: CleanedInvoice):
    insert_invoice_mysql(invoice)
    insert_invoice_mongo(invoice)
    logger.info(f"Submitted invoice from {invoice.vendor} dated {invoice.date}")
    return {"message": "Invoice submitted successfully"}
