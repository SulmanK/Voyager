import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("openai_api_key")
# Set your OpenAI API key
openai.api_key = openai_api_key

def prompt_chatgpt_3_5(prompt):
    try:
        # Send a request to the OpenAI API
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Use gpt-3.5-turbo for the free tier
            prompt=prompt,
            max_tokens=25  # You can adjust this depending on your requirements
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print(f"Error: {e}")
        return None

# Example usage
prompt = "SGD"
response = prompt_chatgpt_3_5(prompt)

print("ChatGPT Response:")
print(response)
