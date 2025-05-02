import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Load Groq API key from .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create a client instance
client = Groq(api_key=GROQ_API_KEY)

def get_llm():
    return client

def generate_response(llm, prompt: str, stop_tokens=None) -> str:
    stop_tokens = stop_tokens or ["Player:"]  # Default stop token

    try:
        # Using chat-style message format
        completion = llm.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.7,
            top_p=0.9,
            stop=stop_tokens  # Pass stop_tokens as stop
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        # More structured error handling
        raise RuntimeError(f"An error occurred while generating the response: {str(e)}")