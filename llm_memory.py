import os
from urllib import response
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")
from languagemodel import LanguageModel, ModelProvider, ModelId

client = OpenAI(api_key=OPEN_AI_API_KEY)
language_model = LanguageModel(
    model_provider=ModelProvider.OPEN_AI,
    model_id=ModelId.OPEN_AI_GPT_4_1_MINI,
    api_key=OPEN_AI_API_KEY,
    temperature=0.1,
)

history = []


def get_llm_response(prompt: str):
    history.append({"role": "user", "content": prompt})
    response = client.responses.create(
        model=language_model.model_id,
        input=[
            {
                "role": "system",
                "content": "You are a precise assistant. Answer in one line only.",
            }
        ]
        + history
        + [
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_output_tokens=100,
        temperature=language_model.temperature,
    )
    history.append({"role": "assistant", "content": response.output_text})
    print(response.output_text)


if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        get_llm_response(user_input)
        print(history)
