# Handoff, Triage
# Triage Agent 가 사용자 요청을 판단 -> 더 적합한 Specialist Agent 에게 대화 책임을 넘기는 , 에이전트 전환 패턴.
# Handoff 는 회사 안내 데스크에서 전문 상담사에게 전화를 넘기는 장면...

from agents import Agent

question_agent = Agent(
    name="question-specialist",
    handoff_description= "면접 질문 생성, 직무별 질문 추천, 난이도별 질문 요청을 처리합니다.",
    instructions="당신은 한국어 면접 질문 출제 전문가 입니다. 질문 2개와 사용 의도를 짧게 제시합니다."
)

scoring_agent = Agent(
    name="scoring_specialist",
    handoff_description="면접 답변 평가, 답변 점검, 개선이 필요한 답변 판정을 처리합니다.",
    instructions="당신은 한국어 면접 답변 평가자입니다. 강점 1개, 보완점 1개를 짧게 제시합니다."
)

triage_agent = Agent(
    name="interview_triage",
    instructions="사용자 요청을 읽고 가장 적합한 Specialist에게 넘기세요.",
    handoffs=[question_agent, scoring_agent]
)

print([agent.name for agent in triage_agent.handsoffs])

# handsoff_description : 내용이 모호하면 에이전트 라우팅이 흔들린다.
# bad_description: 
# - question_specialist: "면접을 도와줍니다."
# - scoring-specialist: "면접을 도와줍니다."