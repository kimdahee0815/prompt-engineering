# 다중 tool 사용 방법
# make_interview_question, score_interview_answer, suggest_follow_up_question

from agents import Agent, Runner
from agents import function_tool
from dotenv import load_dotenv

@function_tool
def make_interview_question(role: str) -> str:
    """지원 직무에 맞는 면접 질문 1개를 만듭니다."""
    print(f"[tool-log] question tool called: role={role}")
    return f"{role} 직무에서 가장 자신 있는 프로젝트를 설명하세요."

@function_tool
def score_interview_answer(answer: str) -> str:
    """면접 답변을 간단히 채점하고 보완점을 반환합니다."""
    print(f"[tool-log] question tool called")
    if "수치" in answer or "%" in answer:
        return "4점: 결과 근거가 있어요. 행동 과정을 조금 더 보완하세요."
    return "2점: 결과 수치나 구체 사례를 추가하세요."

agent = Agent(
    name="optional-two-tool-agent",
    instructions=(
        "질문 생성 요청에는 make_interview_question을 사용하고, "
        "답변 평가 요청에는 score_interview_answer를 사용합니다."
    ),
    tools=[make_interview_question, score_interview_answer]
)    

load_dotenv()

result = Runner.run_sync(
    agent,
    "백엔드 신입 지원자에게 줄 기초 면접 질문을 도구를 사용해서 하나 만들어 주세요.",
    "백엔드 신입 지원자가 제출 한 답변을 간단하게 도구를 사용해서 채점하세요. \n답변: 팀 프로젝트에서 결제 오류를 3일동안 추적해 수정했습니다."
)

print(result.final_output)