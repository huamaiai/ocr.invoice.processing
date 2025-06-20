# OCR engine

# backend/ocr/processor.py

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
from typing import List

def pdf_to_images(pdf_path: str) -> List[Image.Image]:
    """
    Convert a PDF file into a list of PIL Image objects.
    """
    return convert_from_path(pdf_path, dpi=300)

def image_to_text(image: Image.Image) -> str:
    """
    Extract text from a PIL Image using Tesseract.
    """
    return pytesseract.image_to_string(image)

def process_invoice(pdf_path: str) -> str:
    """
    End-to-end processing: Convert PDF to images and extract text from all pages.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Invoice PDF not found: {pdf_path}")
    
    images = pdf_to_images(pdf_path)
    text_blocks = [image_to_text(img) for img in images]
    
    return "\n\n".join(text_blocks)
