import uuid
import json

from Agents.classifier import classify_input
from Agents.email_agent import email_agent
from Agents.json_agent import json_agent
from Memory.view_memory import display

def get_raw_input_somehow():
    return """
Interview Guidelines
Inbox

Sonika M
Tue, May 27, 10:03 AM (2 days ago)
to me


Dear Anurag

Thank you for your interest in joining our team! We’re excited about the possibility of working with you and believe this role can offer you an unparalleled experience in building real-world, real-time trading systems for niche crypto assets.

To ensure a smooth and transparent process, we’ve outlined the interview format and key work expectations below. If you feel these guidelines don’t align with your preferences, please let us know upfront.

Interview Process:
General Technical Round: Basic technical assessment.
Specific Technical Round: Focus on Blockchain and trading bots.
Director Round: Evaluating cultural fit and long-term alignment.

Your next round is scheduled today sharp at 8pm if you're okay with the below shared rules, please join the meeting 

meeting link https://meet.google.com/jea-hfer-fcj

Work Expectations (10 AM - 6 PM, Monday to Saturday):
Transparency: Active video and screen sharing during work hours for better collaboration and communication.
Flexibility: Exceptions can be requested for personal needs for women; group discussions still require active participation.
Teamwork & Proactivity: As part of a fast-paced startup, we value self-starters who can meet deadlines, proactively solve issues, and support their teammates when needed.

Why This Matters:
Trust & Accountability: Transparency builds strong team relationships and ensures clarity in roles and responsibilities.
Enhanced Productivity: Clear communication keeps everyone aligned, reducing delays and enhancing team output.
Innovative Collaboration: Open discussions encourage creativity and innovation in developing cutting-edge systems.

We’re looking forward to seeing you in the next round! Let us know if you have any questions.

NOTE** If you are okay with the above shared details then only join the interview today and also drop a msg on whatsapp to 8309242307 along with your resume

Best regards,
Sonika
"""

def main():
    # Step 1: Get input
    input_text = get_raw_input_somehow()

    # Step 2: Generate unique thread ID
    thread_id = str(uuid.uuid4())

    # Step 3: Your Gemini API Key
    api_key = "AIzaSyBdczkfr5YO7VPz-KR0_EwHa6cTGaoaps0xxxxxxxxxxxxxx"

    print(f"Thread ID: {thread_id}")

    # Step 4: Classify input
    format_intent = classify_input(input_text, api_key=api_key, thread_id=thread_id)
    print(f" Detected Format: {format_intent.format}")
    print(f" Detected Intent: {format_intent.intent}")

    # Step 5: Route to appropriate downstream agent
    if format_intent.format == "Email":
        email_result = email_agent(thread_id, input_text, api_key=api_key)
        print(" Email Agent Result:")
        print(json.dumps(email_result, indent=2))

    elif format_intent.format == "JSON":
        try:
            parsed_json = json.loads(input_text)
            json_result = json_agent(thread_id, parsed_json, api_key=api_key)
            print(" JSON Agent Result:")
            print(json.dumps(json_result, indent=2))
        except json.JSONDecodeError:
            print(" Error: Input marked as JSON but failed to parse.")

    else:
        print(" Unsupported format. No downstream agent available.")

    # Step 6: View entire memory for this thread
    print("\n Full Memory Snapshot:")
    print(json.dumps(display(thread_id), indent=2))


if __name__ == "__main__":
    main()
