from openai import OpenAI

# filepath: /path/to/your/file.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

dad_joke_model = "ft:gpt-4o-2024-08-06:personal:cold-warrior-reasoning:AjVcytwt"


def get_response(messages):
    response = client.chat.completions.create(
        model=dad_joke_model,
        messages=messages
    )
    return response.choices[0].message.content

def main():
    print("Welcome to the Dad Joke Chatbot! Type 'exit' to quit.")
    messages = [{"role": "system", "content": "You are a dad joke expert. Create dad jokes in accordance with the user input."}]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = get_response(messages=messages)
        messages.append({"role": "assistant", "content": response})
        print(f"Dad Joke Bot: {response}")


if __name__ == "__main__":
    main()