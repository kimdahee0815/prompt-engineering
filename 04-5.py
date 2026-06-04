# @function_tool
# Function Calling에서 도구 정의, 호출 감지, 인자 파싱, 파이썬 함수 실행, 실행 결과를 재 메시지 전달.
# @function_tool 회사 인사팀장이 전문가에게 붙여주는 사원증.

def make_interview_question(role, difficulty):
    """role 과 difficulty 만 받아 면접 질문 1개를 반환"""
    if difficulty == "기초":
        return f"{role} 직무에서 최근에 해결한 문제를 한가지 설명하세요."
    if difficulty == "심화":
        return f"{role} 직무에서 장애 상황을 발견했을 때 원인 분석 순서를 설며하세요."
    return f"{role} 직무 지원자로서 본인의 강점을 사례와 함께 말하십시오."

print(make_interview_question("백엔드 신입", "기초"))
print(make_interview_question("데이터 분석 신입", "심화"))