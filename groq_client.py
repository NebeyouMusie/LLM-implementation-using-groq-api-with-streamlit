from groq import Groq
from config import get_groq_api_key

def get_chat_completion(user_input, model):
    client = Groq(
        api_key=get_groq_api_key(),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input or 'introduce your model',
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content
