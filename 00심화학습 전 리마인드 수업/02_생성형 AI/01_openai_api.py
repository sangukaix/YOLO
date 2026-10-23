
# 필요한 모듈 불러오기
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 현재 파이썬 파일과 같은 폴더의 .env 파일 불러오기
env_path = Path(__file__).with_name(".env")
load_dotenv(dotenv_path=env_path, override=True)

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        ".env 파일에 OPENAI_API_KEY를 설정해 주세요."
    )

# OpenAI 객체 생성
client = OpenAI(api_key=api_key)

print("AI 챗봇 시작! (종료: exit)")

# 이전 응답 ID 저장
previous_id = None

while True:
    question = input("\n사용자: ").strip()

    if question.lower() == "exit":
        print("챗봇을 종료합니다. 멍멍!")
        break

    if not question:
        continue

    try:
        # LLM AI 호출 및 응답
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=(
                "당신은 친절한 한국어 AI 챗봇입니다. "
                "당신은 강아지입니다. "
                "모든 답변의 끝에 멍멍!을 붙이세요."
            ),
            input=question,
            previous_response_id=previous_id,
        )

        # 응답 결과 출력
        print("AI:", response.output_text)

        # 다음 질문에서 이전 대화 연결
        previous_id = response.id

    except Exception as e:
        print("오류가 발생했습니다:", e)
