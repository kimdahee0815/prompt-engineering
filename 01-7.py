import os
from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

OPENAI_MODEL = "gpt-5.4-nano"
CLAUDE_MODEL = "claude-haiku-4-5-20251001"
PROMPT = "백엔드 개발자 1차 면접 질문 2개 답변 준비 팁을 짧게 알려줘"

def stream_openai(prompt):
    openai_client = OpenAI()
    
    stream = openai_client.chat.completions.create(
        model="gpt-5.4-nano",
        max_completion_tokens=300,
        messages=[{"role":"user",
               "content":prompt}],
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
        
    print()
    
def stream_claude(prompt):
    anthropic_client = Anthropic()

    with anthropic_client.messages.stream(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{"role":"user",
               "content":prompt}]
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
        
    print()
    
def main():
    load_dotenv()
    print("실행할 스트리밍 프로바이더를 선택하세요.")
    print("1. OpenAI")
    print("2. Claude")
    choice = input("프로바이더 번호 입력: ").strip()
    
    if choice == "1":
        stream_openai(PROMPT)
    elif choice == "2":
        stream_claude(PROMPT)
    else:
        print("1 또는 2만 입력합니다.")