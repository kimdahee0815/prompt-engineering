pct_system="""
## Persona
당신은 한국어로 진행하는 시니어 Python 면접 코치입니다.

## Context
수강자는 Python 3.11 이상을 배우는 초급 비전공 학습자입니다.
면접 질문은 취업 준비생이 바로 연습할 수 있는 수준으로 제시합니다.

## Task
- 기술 면접 질문 2개를 제시합니다.
- 각 질문마다 평가 포인트를 한 문장으로 덧붙이세요.
- 답변은 간결하지만 근거는 빠뜨리지 마세요.

# 큰제목
## 작은제목
### 항목
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL="gpt-5.4-nano"

user_question = "리스트와 튜플 차이를 묻는 면접 질문을 만들어줘"

response = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=250,
    messages=[
        {"role":"developer", "content":pct_system}, # 앞으로는 system 프롬프트 : gpt 내부적으로 (시스템적으로) 사용되는 규칙, 
        # developer 프롬프트 : 개발자가 유저 프롬프트 위에 (앞에) 보다 우선 순위가 높은 규칙 등을 정의하는 프롬프트
        {"role":"user", "content":user_question}
    ]
)

print(response.choices[0].message.content)