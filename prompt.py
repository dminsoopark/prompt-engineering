from openai import OpenAI
import tiktoken
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    print(response)
    return response.choices[0].message.content.strip()

def count_tokens(text):
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = enc.encode(text)
    return len(tokens)

if __name__ == "__main__":
    prompt = "Write an introduction to prompt engineering."
    print("Generated Text:\n", generate_text(prompt))
    print("\nToken Count:", count_tokens(prompt))
