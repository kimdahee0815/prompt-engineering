# stream
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

stream = openai_client.chat.completions.create(
    model="gpt-5.4-nano",
    max_completion_tokens=300,
    messages=[{"role":"user",
               "content":"백엔드 개발자 1차 면접에서 자주 나오는 질문 2개를 알려줘."}],
    stream=True
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
        
print()