from LLm.gemini_client import generate_gemini_response
from Memory.shared_memory import save
import json
import re

EMAIL_AGENT_PROMPT = """
You are a smart email parser that converts emails into CRM-ready format.

Extract the following:
- sender email (if mentioned)
- intent (RFQ, Complaint, Invoice, Interview, etc.)
- urgency (Low, Normal, High)
- summary (brief 1-2 sentence summary)

Email Content:
\"\"\"
{email_text}
\"\"\"

Respond with only raw JSON. Do not include markdown (```), explanations, or formatting.

Example:
{{
  "sender": "someone@example.com",
  "intent": "Interview",
  "urgency": "High",
  "summary": "User invited to an interview with schedule and expectations"
}}
"""

def extract_clean_json(text: str) -> dict:
    try:
        # Remove Markdown-style ```json and ``` wrappers
        cleaned = re.sub(r"```(?:json)?\s*", "", text)
        cleaned = re.sub(r"\s*```", "", cleaned)
        return json.loads(cleaned)
    except Exception as e:
        print(f"[Email Agent] LLM parsing failed: {e}")
        return {
            "sender": "unknown",
            "intent": "Unknown",
            "urgency": "Normal",
            "summary": "LLM parsing failed"
        }

def email_agent(thread_id: str, email_text: str, api_key: str) -> dict:
    prompt = EMAIL_AGENT_PROMPT.format(email_text=email_text)
    response = generate_gemini_response(prompt, api_key)

    print("[Email Agent] Raw LLM output:")
    print(response)

    extracted_json = extract_clean_json(response)

    save(thread_id, {
        "agent": "email_agent",
        "crm_ready": extracted_json,
        "raw_email": email_text
    })

    return extracted_json
