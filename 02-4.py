import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL = "gpt-5.4-nano"

# bad_react= """
# Thought: 좋은 답변입니다.
# Action:
# Observation:
# Answer: 잘했습니다.
# """

# good_react="""
# Thought: 지원하는 협업 경험을 말했지만 성과 수치가 부족합니다.
# Action: 답변 안에서 역할, 행동, 결과가 모두 있는지 확인합니다.
# Observation: 역할과 행동은 보이지만 결과 수치가 없습니다.
# Answer: 결과를 숫자로 보완하면 답변 설득력이 올라갑니다.
# """

reaction_system = """
사용자 질문에 다음 형식으로 답하세요.
Thought: 문제를 분석합니다.
Action: 필요한 정보를 확인합니다.
Observation: 확인 결과를 정리합니다.
Anser: 최종 답변을 한국어로 짧게 씁니다.
"""

question = "면접에서 '협업 경험을 말해주세요'라는 질문에 어떻게 답하면 좋을까요?"

response = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=500,
    messages=[
        {"role":"system", "content":reaction_system},
        {"role":"user", "content":question}
    ]
)

print(response.choices[0].message.content)


