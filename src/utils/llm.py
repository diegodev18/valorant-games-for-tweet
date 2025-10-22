from lib import LLMClient

def generate_text(prompt: str) -> str:
    try:
        response = LLMClient.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Error generating text: {e}")
        return "Error generating text."
