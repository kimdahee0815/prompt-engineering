from agents import Agent
from roles import tech_interviewer_role

question_agent = Agent(
    name="interview_question_agent",
    instructions=tech_interviewer_role + "\n질문은 정확히 3개만 작성하세요."
)

print(question_agent.name)