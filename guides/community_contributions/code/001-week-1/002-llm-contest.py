import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from code.constant import OPENROUTER_BASE_URL, LLM_MODEL


# Load environment variables from .env
load_dotenv()

# Get API key from env variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


def llm_call(model_name, message):
    prompt = [
        {
            "role": "user",
            "content": message,
        }
    ]
    client = OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=API_KEY,
    )
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "Learning Agentic AI",  # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model=model_name,
        messages=prompt,
    )
    return completion


def contest(message, judge, participants):
    contestant_answers = {}

    # Prepare the question to ask the models
    question_response = llm_call(judge, message)
    print(f"Judge Question: {question_response.choices[0].message.content}\n")
    print("*" * 50)
    question = f"{question_response.choices[0].message.content}\nKeep your anser within 100 words and be as concise as possible."

    # Ask the question to each model and store the answers
    for llm in participants:
        print(f"Asking {llm}...")
        response = llm_call(llm, question)
        contestant_answers[llm] = response.choices[0].message.content
        print(f"{llm} answered")

    print("Contestant Answers:")
    print(json.dumps(contestant_answers, indent=2))
    print()
    print("*" * 50)

    # ask judge   to decide winner
    winner_response = llm_call(
        judge,
        f"Based on the following answers, which model provided the best response? \nAnswers: {contestant_answers}",
    )
    winner = winner_response.choices[0].message.content
    print(f"The winner is: {winner}")


if __name__ == "__main__":
    message = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. Answer only with the question, no explanation."
    judge = LLM_MODEL
    participants = [
        "nvidia/nemotron-3-super-120b-a12b:free",
        "meta-llama/llama-3.2-3b-instruct:free",
        "google/gemma-3-27b-it:free",
        "qwen/qwen3-4b:free",
        "mistralai/mistral-small-3.1-24b-instruct:free",
    ]
    contest(message, judge, participants)
