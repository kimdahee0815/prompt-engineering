# Runner
# Agent 를 입력으로해서 실행하고 결과 객체를 돌려주는 실행 관리자.
# - 동기 (Runner.run.sync(...)), 비동기 (await Runner.run(...))
# Agent 는 전문가
# Runner 전문가에게 업무 요청을 배정하고 결과 보고서를 받아오는 매니저.

from agents import Agent
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

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

def main():
    # Runner는 Agent 정의와 사용자 입력을 받아 실제 실행을 담당합니다.
    prompt = "파이썬, FastAPI 프로젝트 경험을 확인하는 면접 질문 3개를 만듭니다."
    result = Runner.run_sync(question_agent, prompt)
    print("[agent]", question_agent.name)
    print("[final_output]", result.final_output)
    

if __name__=="__main__":
    main()