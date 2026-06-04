# OpenAI SDK
# Agents SDK
# Agent: LLM에게 맡길 역할, 지시문, 모델, 도구 사용 등을 담은 실행 주체
# - 면접관 4종 역할 -> 코드 밖으로 분리해 프롬프트를 재사용하기 위한 -> 역할 지시와 도구 호출 코드가 다시 하나의 파일로 섞임.
# - Agent 라는 개념 도입
# Agent 회사에서 새 전문가로 채용할 때 쓰는 직무 기술서와 같은.
from agents import Agent

question_agent_instructions = """
당신은 신입 개발자 면접 질문을 설계하는 기술 면접관입니다.
- 지원자의 프로젝트 경험을 확인하는 질문을 우선합니다.
- 한 번에 질문 3개만 제시합니다.
- 각 질문은 짧고 구체적으로 작성합니다.
- 평가나 피드백은 아직 하지 않습니다.
"""

question_agent = Agent(
    name = "interview_question_agent",
    instructions=question_agent_instructions,
)

print(question_agent.name)
