from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI()

response = client.chat.completions.create(
    model="gpt-5.4-nano",
    max_completion_tokens=300,
    messages=[
        {"role":"system", "content":"당신은 친절한 한국어 ai 면접 코치입니다."},
        {"role":"user", "content":"AI 서비스 개발자 면접 준비를 시작하는 사람에게 첫 조언을 3문장으로 해줘."}
    ]
)
print(response.choices[0].message.content)