import json
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")
from languagemodel import LanguageModel, ModelProvider, ModelId


def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."


# 1. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "get_horoscope",
        "description": "Get today's horoscope for an astrological sign.",
        "parameters": {
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "An astrological sign like Taurus or Aquarius",
                },
            },
            "required": ["sign"],
        },
    },
]

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


def get_horoscope_input(prompt: str) -> list:
    input_list = [
        {
            "role": "system",
            "content": "You are a precise assistant. Answer in one line only.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]
    return input_list


def get_llm_tool_response(prompt: str):
    input_list = get_horoscope_input(prompt)
    response = client.responses.create(
        model=language_model.model_id,
        input=input_list,
        max_output_tokens=100,
        tools=tools,
        temperature=language_model.temperature,
    )
    return response


def handle_tool_calls(response, prompt):
    for item in response.output:
        if item.type == "function_call":
            if item.name == "get_horoscope":
                # 3. Execute the function logic for get_horoscope
                horoscope = get_horoscope(json.loads(item.arguments))

                # 4. Provide function call results to the model
                input_list = get_horoscope_input(prompt)
                input_list.append(
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps({"horoscope": horoscope}),
                    }
                )


if __name__ == "__main__":
    prompt = "What is my horoscope? I am an Aquarius."
    response = get_llm_tool_response(prompt)
    handle_tool_calls(
        response,
        prompt,
    )
    print("Final input:", get_horoscope_input(prompt))
