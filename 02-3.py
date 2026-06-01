# CoT(Chain of Thought)
# Zero-shot, Few-shot 비교
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL = "gpt-5.4-nano"

question = "카페에서 아메리카노 2잔 (4500원), 케이크 1조각 (5500원), 10% 할인 쿠폰, 총 금액은?"

cost_question = question + "\n 단계적으로 생각하여 총 금액을 계산하세요. 마지막 줄에는 최종 금액만 다시 써 주세요."

# (
#     question
#     "우선 아메리카노 2잔 합계를 구하시오."
#     "아메리카노 2잔 합계 금액에 케이크 1조각 금액을 더하시오."
#     "총 금액에 10% 할인을 적용하시오."
#     "최종 금액만 출력하시오."
# )

no_cot = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=200,
    messages=[{"role":"user", "content":question}]
)

with_cot = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=400,
    messages=[{"role":"user", "content":cost_question}]
)

print("[CoT 없이]", no_cot.choices[0].message.content)
print("[CoT 적용]", with_cot.choices[0].message.content)