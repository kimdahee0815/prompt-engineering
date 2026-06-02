from pydantic import BaseModel
from pydantic import Field
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

def generate_interview_question(role, level):
    """질문 생성 도구, 질문 텍스트를 dict로 반환합니다."""
    return {"question":f"{role} 직무에서 {level} 수준의 문제 해결 경험을 설명해 주세요."}

class InterviewScore(BaseModel):
    job_fit: int = Field(ge=0, le=5, description="직무적합 점수")
    problem_solving: int = Field(ge=1, le=5, description="문제해결 점수")
    communication: str = Field(ge=1, le=5, description="전달력 점수")
    attitude: str = Field(ge=1, le=5, description="인성 태도 점수")
    learning: str = Field(ge=1, le=5, description="학습 태도 점수")
    feedback: str = Field(description="개선 피드백")
    
def score_interview_answer(question, answer):
    """채점 도구"""
    answer_length = len(answer.strip())
    base_score = 4 if answer_length >= 30 else 3
    score = InterviewScore (
        job_fit=base_score,
        problem_solving=base_score,
        communication=4,
        attitude=5,
        learning=4,
        feedback= f"질문 '{question[:18]}...' 에 답했어요. 성과 수치와 배운 점을 더하면 좋아요."
    )

tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_interview_question",
        "description": "직무와 난이도에 맞는 면접 질문 1개를 생성합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "role": {"type": "string", "description": "지원 직무"},
                "level": {"type": "string", "description": "질문 난이도"}
            },
            "required": ["role", "level"],
            "additionalProperties": False,
        }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "score_interview_answer",
        "description": "면접 질문과 답변을 받아 InterviewScore 5 필드로 채점합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "면접 질문"},
                "answer": {"type": "string", "description": "지원 답변"}
            },
            "required": ["question", "answer"],
        }
        }
    }
]

tool_map = {
    "generate_interview_question": generate_interview_question,
    "score_interview_answer": score_interview_answer
}

def run_openai():
    load_dotenv()
    client = OpenAI()
    model="gpt-5.4-nano"
    messages=[
        {"role": "system", "content": "면접 코치입니다. 필요한 경우 도구를 호출하세요."},
        {"role":"user", "content": ("백엔드 신입 면접 질문 1개를 만들고, "
                                    "답변 '팀 프로젝트 일정이 밀렸을 때 병목 작업을 나누고 우선순위를 정해 마감했습니다'를 채점해 주세요.")}
        
    ]
    first = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_completion_tokens=500
    )
    assistant_message = first.choices[0].message
    messages.append(assistant_message)
    for tool_call in assistant_message.tool_calls or []:
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        result = tool_map[name](**arguments)
        # if name == "generate_interview_question":
        #     generate_interview_question(**arguments)
        # elif name == "score_interview_answer":
        #     score_interview_answer(**arguments)
        print(f"Using tool: {name}")
        messages.append({
            "role":"tool",
            "tool_call_id":tool_call.id,
            "content":json.dumps(result, ensure_ascii=False)
        })
        if not assistant_message.tool_calls:
            print("[주의] 모델 도구를 호출하지 않았다.")
            return 
        final = client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=500
        )
        print("최종 답변")
        print(final.choices[0].message.content)
        
if __name__ =="__main__":
    run_openai()