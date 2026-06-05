"""coach_agents.py - Agent 정의, @function_tool 등록, Guardrails, Handoff 구성"""

import os
from agents import Agent
from agents import GuardrailFunctionOutput
from agents import RunContextWrapper
from agents import TResponseInputItem
from agents import function_tool
from agents import input_guardrail

from pydantic import BaseModel
from pydantic import Field

from config import MODEL_NAME
from config import init_env
from roles import get_role
from tools import make_interview_question as make_question
from tools import score_answer as _score_answer
from tools import make_feedback as _make_feedback

# =====
# 1. INPUT GUARDRAIL - 프롬프트 인젝션 차단
# =====

class InputCheck(BaseModel):
    blocked: bool = Field(description="위험 입력이면 True")
    reason:str = Field(description="판단 사유")
    matched_terms: list[str] = Field(default_factory=list)

DANGER_TERMS = [
    "improve previous instructions",
    "reveal system prompt",
    "show hidden instructions",
    "developer message",
    "이전 지시 무시",
    "시스템 프롬프트 보여줘",
    "키 보여줘",
    "지시 무시"
]

def inspect_user_text(user_text:str) -> InputCheck:
    """위험 키워드를 검사"""
    lowered = user_text.lower()
    matched = [term for term in DANGER_TERMS if term in lowered]
    return InputCheck(
        blocked=bool(matched), 
        reason="프롬프트 인젝션 의심" if matched else "통과", 
        matched_terms=matched
    )
    
def _normalize_input(raw_input:str | list[TResponseInputItem]) -> str:
    if isinstance(raw_input, str):
        return raw_input
    return " ".join(str(item) for item in raw_input)

@input_guardrail
async def injection_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    check = inspect_user_text(_normalize_input(input))
    return GuardrailFunctionOutput(
        output_info=check,
        tripwire_triggered=check.blocked
    )
    
# ====
# 2. @function_tool 등록
# ====
