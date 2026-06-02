from pydantic import BaseModel
from pydantic import Field

class InterviewScore(BaseModel):
    job_fit: int = Field(ge=0, le=25, description="직무적합 점수")
    problem_solving: int = Field(ge=0, le=20, description="문제해결 점수")
    communication: int= Field(ge=0, le=20, description="전달력 점수")
    attitude: int = Field(ge=0, le=20, description="인성, 태도 점수")
    learning: int = Field(ge=0, le=25, description="학습 태도 점수")
    feedback: str = Field(description="다음 연습에서 고칠 한가지")

sample=InterviewScore(
    job_fit=21,
    problem_solving=16,
    communication=15,
    attitude=18,
    learning=13,
    feedback="결과 수치를 한 문장 더 구체화 하면 좋아요."
)

print(sample.model_dump())

