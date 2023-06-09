import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAPI_KEY")

question = input("Ask your question here: ")

answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": f"{ question }" },
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)