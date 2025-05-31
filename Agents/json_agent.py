from LLm.gemini_client import generate_gemini_response
from Memory.shared_memory import save
import uuid
import json

JSON_AGENT_PROMPT = """
You are a smart JSON processor. Your job is to reformat the incoming JSON into this standard format:
{
  "name": ...,
  "email": ...,
  "product": ...,
  "quantity": ...,
  "date": ...
}

Also, return a list of any missing or invalid fields.

Input JSON:
{input_json}

Respond in valid JSON with two fields:
- "normalized": the cleaned JSON
- "missing_fields": list of missing or invalid fields
"""

def json_agent(thread_id: str, input_json: dict, api_key: str) -> dict:
    prompt = JSON_AGENT_PROMPT.format(input_json=json.dumps(input_json, indent=2))
    response = generate_gemini_response(prompt, api_key)

    try:
        extracted_json = json.loads(response)
        save(thread_id, {
            "agent": "json_agent",
            "normalized": extracted_json.get("normalized", {}),
            "missing_fields": extracted_json.get("missing_fields", []),
            "raw_json": input_json
        })
        return extracted_json
    except Exception as e:
        print(f"[JSON Agent] LLM parsing failed: {e}")
        return {
            "normalized": {},
            "missing_fields": ["LLM parsing failed"]
        }
