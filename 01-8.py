# CLI 루프 구조

def run_cli_loop():
    print("--- 면접 코치 v1 시작 ---")
    print("질문을 입력하세요. 종료하려면 '종료' 또는 'quit'을 입력하세요.")
    
    while True: # 무한 루프 - 종료 명령어가 올때까지 계속 대기
        user_input = input("\n> ").strip() # 앞뒤 공백 제거
        if not user_input:
            print("질문을 입력하세요.")
            continue
        
        if user_input in ("종료", "quit", "exit", "QUIT", "EXIT", "q"):
            print("\n--- 면접 코치 v1 종료 ---")
            break # while 루프 탈출
        
        print(f"[AI 응답 자리]: '{user_input}'에 대한 피드백이 여기에 출력됩니다.")
        
if __name__ == "__main__":
    run_cli_loop()