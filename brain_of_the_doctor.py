import os
import base64
from groq import Groq
from groq._exceptions import GroqError 

# Load environment variable
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY environment variable not set.")

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"Failed to encode image: {e}")

def analyze_image_with_query(query, model, encoded_image):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }
        ]
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Doctor is unavailable right now. Reason: {str(e)}"
