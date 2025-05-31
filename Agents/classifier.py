import re
import json
import uuid
from LLm.gemini_client import generate_gemini_response
from models.format_intent import FormatIntentModel
from Memory.shared_memory import save

CLASSIFIER_PROMPT_TEMPLATE = """
You are a smart classifier. Your job is to detect the format and intent of the user's input.

Input:
\"\"\"
{input_text}
\"\"\"

Respond in **valid JSON** with two fields:
- "format": one of ["Email", "JSON", "PDF", "Unknown"]
- "intent": one of ["Invoice", "Complaint", "RFQ", "Regulation", "Unknown"]
"""

def classify_input(input_text: str, api_key: str, thread_id: str = None) -> FormatIntentModel:
    if not thread_id:
        thread_id = str(uuid.uuid4())

    prompt = CLASSIFIER_PROMPT_TEMPLATE.format(input_text=input_text)
    response_text = generate_gemini_response(prompt, api_key)

    try:
        json_block = re.search(r'\{.*?\}', response_text, re.DOTALL).group()
        parsed = json.loads(json_block)
        model = FormatIntentModel(**parsed)
    except Exception as e:
        print(f"[Classifier] Error parsing LLM response: {e}")
        model = FormatIntentModel(format="Unknown", intent="Unknown")

    # Save to persistent memory
    save(thread_id, {
        "agent": "classifier_agent",
        "format": model.format,
        "intent": model.intent,
        "raw_text": input_text
    })

    return model
