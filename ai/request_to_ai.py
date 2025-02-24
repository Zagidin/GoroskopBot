from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=getenv("API_KEY_AI"),
)

def request_to_ai(message_content):
  """
    models:
        1) cognitivecomputations/dolphin3.0-mistral-24b:free 🚩
        2) cognitivecomputations/dolphin3.0-r1-mistral-24b:free ✅
        3) google/gemini-2.0-pro-exp-02-05:free
        4) google/gemini-2.0-flash-lite-preview-02-05:free
        5) deepseek/deepseek-r1-distill-llama-70b:free
        6) qwen/qwen2.5-vl-72b-instruct:free 🚩
  """
  completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
      {
        "role": "user",
        "content": f"{message_content}"
      }
    ]
  )

  return completion.choices[0].message.content


# print(request_to_ai("Прием Прием!"))