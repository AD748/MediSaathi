import ollama
import json
from agent.prompt.system_prompt import SYSTEM_PROMPT


def extract_intent(user_text):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    text = response["message"]["content"]

    try:
        return json.loads(text)
    except:
        return {"intent": "unknown"}