# Function Calling : 모델에게 호출 가능한 함수 목록과 각 함수가 받을 인자 규칙을 JSON 형태로 알려주고,
# 모델이 상황에 맞는 함수를 호출 요청을 만들게 하는 방법.

import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def score_interview_answer(answer, job_role):
    """단순 규칙으로 채점해서 도구 호출 흐름에 집중"""
    # 숫자와 협업 표현 있는지 확인. -> 예시 점수를 높임.
    has_metric = any(char.isdigit() for char in answer)
    has_collaboration = "팀" in answer or "협업" in answer
    score = 8 if has_metric and has_collaboration else 6
    return {
        "overall_score": score,
        "job_role": job_role,
        "feedback": "성과 수치와 협업 맥락을 함께 말하면 더 좋아요."
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "score_interview_answer",
        "description": "신입 지원자의 면접 답변을 직무 기준에 맞춰 채점합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "answer": {"type": "string", "description": "지원자의 면접 답변"},
                "job_role": {"type": "string", "description": "지원 직무"}
            },
            "required": ["answer", "job_role"],
            "additionalProperties": False,
        }
        }
    }
]

candidate_answer = "팀 프로젝트에서 결제 오류를 3일 동안 추적해 수정했습니다."
messages = [
    {"role": "system", "content": "당신은 신입 개발자 면접 답변을 평가하는 면접 코치입니다."},
    {"role": "user", "content": f"백엔드 신입 지원자의 답변을 채점하고 피드백해 주세요. \n답변: {candidate_answer}"}
]

first = client.chat.completions.create(
    model="gpt-5.4-nano",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

assistant_message = first.choices[0].message
tool_calls = assistant_message.tool_calls or []
print(f"tool_calls detected: {len(tool_calls)}")

if not tool_calls:
    print("도구 호출이 없어서 모델 응답을 그대로 확인 합니다.")
    print(assistant_message.content)
else:
    messages.append(assistant_message)

    for tool_call in tool_calls:
        arguments = json.loads(tool_call.function.arguments)
        print("function arguments: ")
        print(json.dumps(arguments, ensure_ascii=False, indent=2))

        if tool_call.function.name != "score_interview_answer":
            raise ValueError(f"알 수 없는 도구: {tool_call.function.name}")

        result = score_interview_answer(**arguments)
        print("tool result: ")
        print(json.dumps(result, ensure_ascii=False, indent=2))

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, ensure_ascii=False),
            }
        )

    final = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages= messages
    )

    print("final answer")
    print(final.choices[0].message.content)
