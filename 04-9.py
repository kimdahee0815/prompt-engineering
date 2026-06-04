# Handoff, Triage
# Triage Agent 가 사용자 요청을 판단 -> 더 적합한 Specialist Agent 에게 대화 책임을 넘기는 , 에이전트 전환 패턴.
# Handoff 는 회사 안내 데스크에서 전문 상담사에게 전화를 넘기는 장면...

from agents import Agent
from agents import Runner

question_agent = Agent(
    name="question-specialist",
    handoff_description= "면접 질문 생성, 직무별 질문 추천, 난이도별 질문 요청을 처리합니다.",
    instructions=(
        "당신은 한국어 면접 질문 출제 전문가 입니다."
    "요청 직무에 맞는 질문 2개와 질문의 확인 포인트를 짧게 제시합니다."
    )
)

scoring_agent = Agent(
    name="scoring_specialist",
    handoff_description="면접 답변 평가, 답변 점검, 개선이 필요한 답변 판정을 처리합니다.",
    instructions=(
        "당신은 한국어 면접 답변 평가자입니다."
        "강점 1개, 보완점 1개를 다음 연습 문장 1개 짧게 제시합니다."
        )
)

triage_agent = Agent(
    name="interview_triage",
    model="gpt-5.4-nano",
    instructions=(
        "사용자 요청을 읽고 질문 생성이면 question_specialist",  
        "면접 답변 평가나 개선 요청이면 scoring_specialist"
    ),
    handoffs=[question_agent, scoring_agent]
)

# print([agent.name for agent in triage_agent.handsoffs])

# handsoff_description : 내용이 모호하면 에이전트 라우팅이 흔들린다.
# bad_description: 
# - question_specialist: "면접을 도와줍니다."
# - scoring-specialist: "면접을 도와줍니다."
import asyncio

async def run_case(user_request: str) -> None:
    result = await Runner.run(triage_agent, user_request)
    print("=" * 50)
    print(f"[user] {user_request}")
    print(f"[selected_agent] {result.last_agent.name}")
    print(f"[summary] {str(result.final_output[:1000])}")
    
async def main() -> None:
    await run_case("백엔드 신입 면접 질문을 2개 만들어줘.")
    await run_case("이 답변을 평가해줘: 저는 장애가 나면 로그부터 확인하고 원인을 좁혀갑니다.")
    
if __name__ == "__main__":
    main()