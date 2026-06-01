import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_MODEL = "gpt-5.4-nano"

react_system={
    "role":"system",
    "content":"Thought, Acion, Observation, Answer 형식으로 한국어 피드백을 작성합니다."
}

few_shot_messages=[
    react_system,
    {"role":"user", "content":"협업 경험 답변에 결과가 없습니다. 어떻게 피드백할까요?"},
    {"role":"assistant","content":
        """
            Thought: 결과 수치가 빠져 있습니다.
            \nAction: 행동 뒤 성과가 있는지 확인합니다.
            \nObservation: 성과가 없어서 설득력이 약합니다.
            \nAnswer: 협업 결과를 숫자나 변화로 보완하게 안내합니다.
        """},
    {"role":"user", "content":"실패 경험 답변에 배운 점이 없습니다. 어떻게 피드백할까요?"}
]

response = client.chat.completions.create(
    model=OPENAI_MODEL,
    max_completion_tokens=300,
    messages=few_shot_messages  
)

print(response.choices[0].message.content)