import os

from groq import Groq # type: ignore

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Qual a maior empresa do mundo ?",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)