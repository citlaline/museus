from groq import Groq
import streamlit as st

api_key = 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

client = Groq(api_key=api_key)
    model="llava-v1.5-7b-4096-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": ""
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "${IMAGE_DATA_URL}"
                    }
                }
            ]
        }
    ],
    temperature=0.5,
    max_tokens=3000,
    top_p=0.9,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
