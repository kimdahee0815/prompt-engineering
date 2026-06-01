# stream
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

anthropic_client = Anthropic()

with anthropic_client.messages.stream(
    model="claude-haiku-4-5-20251001",
    max_tokens=300,
    messages=[{"role":"user",
               "content":"백엔드 개발자 1차 면접에서 자주 나오는 질문 2개를 알려줘."}]
) as stream:
    for chunk in stream.text_stream:
        print(chunk, end="", flush=True)
        
    print()