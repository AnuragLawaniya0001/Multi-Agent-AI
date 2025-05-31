from pydantic import BaseModel
from typing import Literal

class FormatIntentModel(BaseModel):
    format: Literal["Email", "JSON", "PDF", "Unknown"]
    intent: Literal["Invoice", "Complaint", "RFQ", "Regulation", "Unknown"]
