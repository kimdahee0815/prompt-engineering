from dotenv import load_dotenv
from agents import Agent, Runner
from roles import tech_interview_prompts

load_dotenv()

ROLE="당신은 신입 개발자 기술 면접관입니다."
CONTEXT="지원자는 파이썬과 FASTAPI 프로젝트 경험을 가진 취업 준비생입니다."
TASK="프로젝트 경험을 확인하는 면접 질문을 정확히 3개 작성합니다."
CONSTRAINTS="평가, 피드백, 모범답안은 아직 작성하지 마세요."

question_agent = Agent(
    name="interview_question_agent",
    #instructions="\n".join([ROLE, CONTEXT, TASK, CONSTRAINTS])
    instructions=tech_interview_prompts()
)

def main():
    user_input = "백엔드 신입 지원자의 API 개발 경험을 확인하고 싶어요."
    result = Runner.run_sync(question_agent, user_input)
    print(question_agent.name)
    print(result.final_output)
    
if __name__ == "__main__":
    main()