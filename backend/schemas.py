from pydantic import BaseModel
from typing import Optional

class CleanedInvoice(BaseModel):
    vendor: str
    date: str
    total: str
    notes: Optional[str]
    raw_text: str