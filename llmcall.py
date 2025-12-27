import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ.get("HF_TOKEN")
)

def call_llm(prompt, temperature=0):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

def call_llm_json(prompt, temperature=0, retries=3, delay=2):
    last_error = None

    for _ in range(retries):
        try:
            output = call_llm(prompt, temperature)
            return json.loads(output)
        except Exception as error:
            last_error = error
            time.sleep(delay)

    raise last_error
