from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client=Anthropic()

score_tool = {
    "name": "submit_interview_score",
    "description": "면접 답변을 5개 채점 항목으로 평가하여 점수를 제출합니다.",
    "input_schema": {
        "type": "object",
        "properties": {
            "직무적합": {"type": "integer", "description":"직무 관련 역량 점수 (1-10)"},
            "문제해결": {"type":"integer", "description": "문제 해결 능력 점수 (1-10)"},
            "커뮤니케이션": {"type":"integer", "description": "의사 소통 능력 점수 (1-10)"},
            "인성": {"type":"integer", "description": "협업 태도 신뢰성 점수 (1-10)"},
            "학습잠재력": {"type":"integer", "description": "성장 가능성 자기계발 점수 (1-10)"}
        },
        "required": ["직무적합", "문제해결", "커뮤니케이션", "인성", "학습잠재력"]
    }
}