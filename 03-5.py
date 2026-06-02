import os
from dotenv import load_dotenv
from anthropic import Anthropic

def get_interview_hint(answer):
    if "결과" not in answer and "수치" not in answer:
        return "프로젝트 결과나 수치를 한 문장 추가해 보세요."
    return "상황, 행동, 결과가 드러나므로 다음 질문으로 이어갈 수 있어요."

tools = [
    {"name": "get_interview_hint",
     "description": "면접 답변에서 바로 보완할 힌트 한 줄을 반환합니다.",
     "input_schema":{
         "type":"object",
         "properties": {
             "answer": {"type": "string", "description":"지원자 답변"}
         },
         "required":["answer"]
     }}
]

load_dotenv()
client=Anthropic()

user_message = "다음 면접 답변의 보완 힌트를 도구로 확인 해 보세요: 로그를 보고 오류를 고쳤습니다."

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=300,
    tools=tools,
    messages=[
        {"role":"user", "content":user_message}
    ]
)

if response.stop_reason != "tool_use":
    raise RuntimeError(f"도구 호출 감지되지 않았어요: {response.stop_reason}")

tool_user = next(block for block in response.content if block.type=="tool_use")
print(f"tool_name={tool_user.name}")
print(f"tool_name={tool_user.id}")
print(f"tool_name={tool_user.input}")