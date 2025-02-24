"""
    Сделать БД ссылками на AI не рабочие указывать под 0 рабочие под 1 и проводить фильтрацию с выводом рабочих
"""

from os import getenv
from openai import OpenAI
# from random import randint
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=getenv("API_KEY_AI"),
)

# free_ai = [
#   "cognitivecomputations/dolphin3.0-mistral-24b:free", "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
#   "google/gemini-2.0-pro-exp-02-05:free", "google/gemini-2.0-flash-lite-preview-02-05:free",
#   "qwen/qwen2.5-vl-72b-instruct:free", "deepseek/deepseek-r1-distill-llama-70b:free",
#   "google/gemini-2.0-flash-lite-preview-02-05:free"
# ]

def request_to_ai(message_content):
  """
    models:
        1) cognitivecomputations/dolphin3.0-mistral-24b:free 🚩
        2) cognitivecomputations/dolphin3.0-r1-mistral-24b:free ✅ шо то не робит лимит запросов скорее всего
        3) google/gemini-2.0-pro-exp-02-05:free
        4) google/gemini-2.0-flash-lite-preview-02-05:free
        5) deepseek/deepseek-r1-distill-llama-70b:free
        6) qwen/qwen2.5-vl-72b-instruct:free ✅🚩 <- норм справляется
  """
  completion = client.chat.completions.create(
    model="qwen/qwen2.5-vl-72b-instruct:free", # free_ai[randint(0, len(free_ai))]
    messages=[
      {
        "role": "user",
        "content": f"{message_content}"
      }
    ]
  )

  return completion.choices[0].message.content


# print(request_to_ai("Прием Прием!"))