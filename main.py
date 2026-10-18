import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Find the .env file beside main.py
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Read the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key or not api_key.strip():
    print("Groq API key is missing. Check your .env file.")
    raise SystemExit(1)

# Create the Groq client
client = Groq(api_key=api_key)

# Ask the AI a question
try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are StudyMate AI, a helpful study assistant."
            },
            {
                "role": "user",
                "content": input("Enter your question")
            }
        ]
    )

    print("\nStudyMate AI:")
    print(response.choices[0].message.content)

except Exception as error:
    print("Groq request failed.")
    print("Error type:", type(error).__name__)
    print("Error details:", str(error))