import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL = "gpt-5.4-nano"

cot_prompt="단계적으로 생각하여 면접 답변을 피드백하세요."
react_system=f"""
    {cot_prompt}
    단, 답변은 아래 형식으로 제한합니다.
    Thought: 판단 기준을 세웁니다.
    Action: 답변에서 확인할 정보를 정합니다.
    Observation: 확인 결과를 적습니다.
    Answer: 최종 피드백을 제시합니다.
"""
cot_messages=[
    {
        "role":"system",
        "content":react_system
    },
    {
        "role":"user",
        "content":"실패 경험 답변에 배운 점이 없습니다. 어떻게 피드백할까요?"
    }
]

response = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=300,
    messages=cot_messages  
)

print(response.choices[0].message.content)