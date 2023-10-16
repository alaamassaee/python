import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("What question do you have to OpenAI?")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": prompt
    }
  ],
  temperature=0.5,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
