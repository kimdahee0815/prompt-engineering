# Zero-shot, Few-shot 비교
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL = "gpt-5.4-nano"

target_review = "배송은 빠른데 포장이 엉망이에요."

zero_shot = [
    {
        "role":"user",
        "content": f"다음 리뷰의 감정을 분류하세요: '{target_review}'"
    }
]

few_shot = [
    {
        "role":"user",
        "content": f"리뷰: '마음에 들어요 잘 사용하고 있습니다.' -> 감정: "
    },
    {
        "role":"assistant",
        "content": f"긍정"
    },
    {
        "role":"user",
        "content": f"리뷰: '환불 요청했는데 연락이 안됩니다.' -> 감정: "
    },
    {
        "role":"assistant",
        "content": f"부정"
    },
    {
        "role":"user",
        "content": f"리뷰: '{target_review}' -> 감정: "
    }
]

openai_zero = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=80,
    messages=zero_shot
)

openai_few = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=80,
    messages=few_shot
)
print(f"[Zero-shot]", openai_zero.choices[0].message.content)
print(f"[Few-shot]", openai_few.choices[0].message.content)