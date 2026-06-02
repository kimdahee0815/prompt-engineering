from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client=Anthropic()

score_tool = {
    "name": "submit_interview_score",
    "description": "면접 답변을 5개 채점 항목으로 평가하여 점수를 제출합니다.",
    "input_schema": {
        "type": "object",
        "properties": {
            "job_fit": {"type": "integer", "description":"직무 관련 역량 점수 (1-10)"},
            "problem_solving": {"type":"integer", "description": "문제 해결 능력 점수 (1-10)"},
            "communication": {"type":"integer", "description": "의사 소통 능력 점수 (1-10)"},
            "personality": {"type":"integer", "description": "협업 태도 신뢰성 점수 (1-10)"},
            "learning_agility": {"type":"integer", "description": "성장 가능성 자기계발 점수 (1-10)"}
        },
        "required": ["job_fit", "problem_solving", "communication", "personality", "learning_agility"]
    }
}

interview_answer = """
저는 파이썬으로 데이터 파이프라인을 구축하는 프로젝트를 3개 진행했습니다.
팀원과 코드 리뷰를 통해 소통했고, 막히는 부분은 공식 문서를 먼저 찾아
해결하는 편입니다.
"""

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=512,
    system="당신은 AI 기업 면접관입니다. 지원자의 답변을 5개 항목으로 채점하세요.",
    tools=score_tool,
    tool_choice={"type":"tool", "name":"submit_interview_score"},
    messages=[
        {"role":"user", "content": f"다음 답변을 채점하세요: \n{interview_answer}"}
    ]
)

print("stop_reason: ", response.stop_reason) # "tool_use" 인지 확인

tool_use_blok = next(b for b in response.content if b.type == "tool_use")
scores = tool_use_blok.input

for field, score in scores.items():
    print(f"{field}: {score}")