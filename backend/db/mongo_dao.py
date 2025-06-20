from pymongo import MongoClient
import os

def insert_invoice_mongo(invoice):
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db = client[os.getenv("MONGO_DB", "invoice_logs")]
    collection = db["raw_ocr_logs"]

    collection.insert_one({
        "vendor": invoice.vendor,
        "date": invoice.date,
        "total": invoice.total,
        "notes": invoice.notes,
        "raw_text": invoice.raw_text
    })