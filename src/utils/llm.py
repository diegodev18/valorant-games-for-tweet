from lib import LLMClient
from google.genai import types

def generate_text(prompt: str) -> str:
    try:
        systemInstructions = [
            types.Content(
                role="system",
                parts=[types.Part(text="""\
You are an Agent for automated text generation. Make a message about Valorant Games based on the user's prompt.

Be creative and use your knowledge of Valorant to craft an engaging message.

Text should be in Spanish. Use emoticons where appropriate to enhance the message. And be friendly and engaging in tone. Use informal language. Don't use bad words. Use hashtags related to Valorant and gaming for Twitter.
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
