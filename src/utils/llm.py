from lib import LLMClient
from google.genai import types

def generate_text(prompt: str) -> str:
    try:
        systemInstructions = [
            types.Content(
                role="system",
                parts=[types.Part(text="""\
You are an Agent for automated text generation. Make a message about Valorant Games based on the user's prompt.\
    """)],
            )
        ]
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=prompt)]
            )
        ]
        response = LLMClient.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            systemInstructions=systemInstructions,
        )
        return response.text
    except Exception as e:
        print(f"Error generating text: {e}")
        return "Error generating text."
