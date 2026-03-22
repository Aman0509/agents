import os
from dotenv import load_dotenv
from openai import OpenAI
from code.constant import OPENROUTER_BASE_URL, LLM_MODEL


# Load environment variables from .env
load_dotenv()

# Get API key from env variable
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url=OPENROUTER_BASE_URL,
    api_key=api_key,
)

completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "Learning Agentic AI",  # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model=LLM_MODEL,
    messages=[{"role": "user", "content": "Which is the best cricket team ever?"}],
)
print(completion.choices[0].message.content)
