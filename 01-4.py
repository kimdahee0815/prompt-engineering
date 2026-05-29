import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

print("=" * 50)
print (" OpenAI Responses API 대화 루프")
print(" 종료하려면 '9999'를 입력하세요.")
print("=" * 50)
print()

previous_id=None
turn = 0

while True:
    user_input = input("질문: ").strip()
    if user_input == "9999":
        print("\n대화를 종료합니다. 안녕~~~")
        break
    if not user_input:
        print("빈 입력입니다. 질문을 다시 입력하세요.\n")
        continue
    turn += 1
    responses = client.responses.create(
        model="gpt-5.4-mini",
        max_output_tokens=500,
        input=user_input,
        **({"previous_response_id": previous_id} if previous_id else {})
    )

    answer = responses.output_text.strip()
    if not answer:
        print("응답이 비어 있습니다. 다시 질문하세요.")
        continue
    print(f"\n [{turn}]차 응답 {answer}\n")
        