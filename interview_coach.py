"""interview_coach.py - AI 면접 코치 CLI 프로그램"""
import asyncio
import sys
import time
from dataclasses import dataclass, field
from agents import InputGuardrailTripwireTriggered, Runner
from config import MODEL_NAME, init_env
from role import DEFAULT_ROLE_KEY, list_roles
from coach_agents import triage_agent

# =====
# Trace 로깅 유틸
# =====

# =====
# CLI 명령어 처리
# =====

COMMANDS={
    "/help": "사용 가능한 명령어를 보여줍니다.",
    "/quit": "면접 코치를 종료합니다.",
    "/role": "면접관 유형 목록을 보여줍니다.",
    "/set": "면접관 유형을 변경합니다. 예: /set personality",
    "/trace": "마지막 응답의 실행 추적 로그 보여줍니다. (미구현)"
}

def show_help() -> None:
    pass

def show_roles() -> None:
    pass

# ====
# Agent 실행 래퍼
# ====
async def run_agent(user_input:str) -> str:
    """Triage agent 를 통해 사용자 입력 처리"""
    try:
        result = await Runner.run(triage_agent, user_input)
        last_agent_name = result.last_agent.name
        return f"[{last_agent_name}]\n{result.final_output}"
    except InputGuardrailTripwireTriggered:
        return (
            "안전하지 않은 입력이 감지되었습니다.\n"
            "면접 관련 질문을 다시 입력하세요."
        )
    except Exception as errors:
        return f"오류가 발생했습니다. {type(errors).__name__}\n {errors}"

# ====
# Main CLI Loop
# ===

def main() -> None:
    print()
    print("=" * 50)
    print("    면접 코치")
    print("=" * 50)
    
    # 환경점검
    if not init_env():
        print("\n .env 파일을 설정한 뒤 다시 실행하세요")
        sys.exit(1)
    print(f"   모델: {MODEL_NAME}")
    print(f"        기본 면접관: {DEFAULT_ROLE_KEY}")
    print("         /help 로 명령어를 확인하세요.\n")
    
    while True:
        user_input = input("    >").strip()
        if not user_input:
            continue
        if user_input == "/quit":
            print("\n 면접 코치를 종료합니다. 수고하셨습니다.")
            break
        if user_input == "/help":
            show_help()
            continue
        if user_input == "/role":
            show_roles()
            continue
        if user_input.startswith("/"):
            print(" 알 수 없는 명령어", {user_input})
            print("/help로 사용 가능한 명령어를 확인합니다.")
            continue
        print("면접 코치가 응답을 준비하고 있습니다...")
        response = asyncio.run(run_agent(user_input))
        print(f"  {response}")
        
if __name__ == "__main__":
    main()