from pydantic import BaseModel
from pydantic import Field
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

class InterviewScore(BaseModel):
    job_fit: int = Field(ge=0, le=25, description="직무적합 점수")
    overall_score: int = Field(ge=1, le=10)
    clarity: str
    improvement_points: list[str]
    follow_up_question: str

candidate_answer="""
저는 팀 프로젝트에서 결제 API 오류를 맡았습니다.
처음에는 원인을 못 찾았지만 로그를 나눠 보고, 재현 조건을 정리해서
프론트엔드 팀과 함께 예외 처리를 수정했습니다.
"""

completion = client.chat.completions.parse(
    model="gpt-5.4-nano",
    messages=[
        {"role":"system", "content":"당신은 신입 백엔드 개발자 면접 답변을 채점하는 면접 코치입니다."},
        {"role":"user", "content":f"다음 답변을 채점해 주세요 \n\n{candidate_answer}"}
    ],
    response_format=InterviewScore
)

message = completion.choices[0].message
print(type(message.parsed).__name__)
print(json.dumps(message.parsed.model_dump(), ensure_ascii=False, indent=2))
