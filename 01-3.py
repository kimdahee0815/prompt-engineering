# Responses API
# chat completions의 응답 messages 배열로 구성되어 있다.
# previous_response_id

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

r1 = client.responses.create(
    model="gpt-5.4-nano",
    max_output_tokens=300,
    input="백엔드 개발자 1차 면접에서 처음 던질 질문을 하나 만들어 주세요."
)
print("1차: ",r1.output_text)

r2 = client.responses.create(
    model="gpt-5.4-nano",
    max_output_tokens=300,
    input="방금 질문을 신입 지원자가 이해하기 쉽게 한 문장으로 바꿔서 작성하세요.",
    previous_response_id=r1.id
)
print("2차: ", r2.output_text)

first_text = r1.output_text.strip()
second_text = r2.output_text.strip()

print(first_text)
print(second_text)