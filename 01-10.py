# 면접 코치 페르소나
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# system 메시지 : 면접관 역할 지정 (한 번 정의하고 루프 내내 재사용)
system_message = {
    "role": "system",
    "content": (
        "당신은 친절하지만 정확한 면접관입니다."
        "사용자가 입력한 면접 질문이나 답변을 바탕으로"
        "구체적이고 건설적인 피드백을 한국어로 제공합니다."
        "답변은 3 ~ 5 문장으로 간결하게 유지합니다"
    )
}

# 대화 히스토리 : 처음은 system 메시지로 시작 -> 루프마다 user/assistant 추가
conversation = [system_message]

def get_ai_response(user_input):
    """사용자 입력을 messages에 추가하고 AI 응답 반환"""
    conversation.append({"role":"user", "content":user_input})
    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        max_completion_tokens=400, # GPT-5 계열: max_completion_tokens, 5 이전 계열: max_tokens
        messages=conversation,
        stream=True
    )
    
    full_response=""
    print("\n[코치] > ", end="", flush=True)
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            full_response += delta
    print()
    
    conversation.append({"role": "assistant", "content": full_response}) # AI 응답 추가
    return full_response

def run_interview_coach():
    """면접 코치 v1 메인 루프"""
    print("=" * 50)
    print(" AI 면접 코치 v1 시작")
    print(" 면접 질문이나 답변을 입력하세요.")
    print(" 종료: '종료', 'quit' 입력")
    print("=" * 50)
    
    while True:
        user_input = input("\n[나] > ").strip()
        if not user_input:
            print(" (입력이 없습니다. 질문이나 답변을 입력해주세요.)")
            continue
        if user_input.lower() in ("종료", "quit"):
            print("\n--- 면접 코치 v1 종료 ---")
            break
        get_ai_response(user_input)

    
if __name__ == "__main__":
    run_interview_coach()