from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

# client=OpenAI()
client = Anthropic()

# response = client.chat.completions.create(
#     model="gpt-5.4-nano",
#     max_completion_tokens=300,
#     messages=[
#         {"role":"system", "content":"당신은 친절한 한국어 ai 면접 코치입니다."},
#         {"role":"user", "content":"AI 서비스 개발자 면접 준비를 시작하는 사람에게 첫 조언을 3문장으로 해줘."}
#     ]
# )
# print(response.choices[0].message.content)

response = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=300,
    system="당신은 친절한 한국어 ai 면접 코치입니다.",
    messages=[
        {"role":"user", "content":"AI 서비스 개발자 면접 준비를 시작하는 사람에게 첫 조언을 3문장으로 해줘."}
    ]
)

print(response.content[0].text)

# 프롬프트
# - system prompt: 모델에게 "어떤 사람처럼 답할지 (페르소나)", "무엇을 우선할지", "어떤 경계를 지킬지", "답을 한국어로 합니다."
# - user prompt: 

# max_tokens
# 답변이 길어질 수록 시간과 비용이 늘어난다. 면접 코치 (질문과 피드백을 여러번 주고 받는 서비스), 한 번의 답변 길이를 적당히 제한 해야.
# gpt-5: max_completion_tokens
# claude: max_tokens
# 빠른 답변이 필요할 때. (답변은 1분 안에 하세요.) 너무 작게 설정하면 (응답의 품질이 저하)
# 인풋 토큰, 아웃풋 토큰 (output token gpt: max_output_tokens)

# content[0].text
# 응답 본문을 가져온다.