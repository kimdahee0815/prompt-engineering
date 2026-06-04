from agents import Agent
from agents import function_tool
from dotenv import load_dotenv
from agents import Runner
import asyncio

@function_tool
def make_interview_question(role, difficulty):
    """지원 직무와 난이도를 받아 면접 질문 1개를 만듭니다.
    Args:
        role: 지원 직무 이름입니다. 예: 백엔드 신입, 데이터 분석 신입
        difficulty: 질문 난이도입니다. 예: 기초, 심화
    """
    
    print(f"[tool-log] make_interview_question called: role={role}, difficulty={difficulty}")
    if difficulty == "기초":
        return f"{role} 직무에서 최근에 해결한 문제를 한가지 설명하세요."
    if difficulty == "심화":
        return f"{role} 직무에서 장애 상황을 발견했을 때 원인 분석 순서를 설며하세요."
    return f"{role} 직무 지원자로서 본인의 강점을 사례와 함께 말하십시오."

async def main():
    interview_agent = Agent(
        name="interview-question-agent",
        model="gpt-5.4-nano",
        instructions=(
            "당신은 한국어 면접 코치입니다. 사용자가 면접 질문 생성을 요청하면"
            "반드시 make_interview_question 도구를 사용한 뒤 결과를 짧게 설명하세요."
        ),
        tools=[make_interview_question]
    )

    # print(interview_agent.name)
    # print(interview_agent.tools)

    load_dotenv()

    result = await Runner.run(
        interview_agent,
        "백엔드 신입 지원자에게 줄 기초 면접 질문을 도구를 사용해서 하나 만들어 주세요."
    )
    
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())