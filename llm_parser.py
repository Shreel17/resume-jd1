from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def parse_resume(text: str) -> dict:
    prompt = f"""
Extract structured resume data in JSON with the following fields:
- name
- skills
- experience
- education
- projects

Return ONLY valid JSON.
Do NOT include markdown.
Do NOT include explanations.

Resume:
{text}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    # In new SDK, this is the correct way
    content = response.output_text

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"LLM returned invalid JSON.\nError: {e}\n\nRaw output:\n{content}"
        )



