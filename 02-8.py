import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL="gpt-5.4-nano"

def find_instruction_conflicts(system_prompt):
    """수업용 단순 검사: 함께 있으면 흔들릴 수 있는 지시 쌍을 찾아요"""
    conflict_pairs = [
        ("한 문장", "상세히"),
        ("짧게", "자세히"),
        ("답만", "근거"),
        ("무조건", "예외")
    ]
    found: list[str] = []
    for left, right in conflict_pairs:
        if left in system_prompt and right in system_prompt:
            found.append(f"'{left}' 지시와 '{right}' 지시가 함께 있어요.")
    return found

pct_system="""## Persona
당신은 한국어로 진행하는 시니어 Python 면접 코치입니다.

## Context
수강자는 Python 3.11 이상을 배우는 초급 비전공 학습자입니다.
면접 질문은 취업 준비생이 바로 연습할 수 있는 수준으로 제시합니다.
답만 간단하게 필요한 상황이다.

## Task
- 기술 면접 질문 2개를 제시합니다.
- 각 질문마다 평가 포인트를 한 문장으로 덧붙이세요.
- 답변은 3문장 이내로 유지하고, 판단 근거는 bullet 2개 덧붙이세요.
"""

user_question = "리스트와 튜플 차이를 묻는 면접 질문을 만들어줘."

def run_pct(system_prompt, question):
    """OpenAI developer role에 앱 기준 지시를 둔다"""
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=250,
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    print(response.choices[0].message.content)

def main():
    conflicts = find_instruction_conflicts(pct_system)
    print("충돌 점검", conflicts if conflicts else "충돌 후보 없음")
    run_pct(system_prompt=pct_system, question=user_question)
    
    
if __name__ == "__main__":
    main()