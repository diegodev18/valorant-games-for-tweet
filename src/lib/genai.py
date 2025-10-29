from google import genai
from utils.get_env import get_env

GOOGLE_API_KEY = get_env("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY no está configurada en las variables de entorno.")

GENAI_CLIENT = genai.Client(api_key=GOOGLE_API_KEY)
