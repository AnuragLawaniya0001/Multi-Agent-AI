import google.generativeai as genai

def generate_gemini_response(prompt: str, api_key: str) -> str:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            return response.text.strip()
        elif hasattr(response, "parts"):
            return "".join(part.text for part in response.parts).strip()
        else:
            return "No valid response"
    except Exception as e:
        return f"Error generating Gemini response: {str(e)}"
