"""FastAPI 실습 예비 파일.

현재 이 파일은 빈 파일로 남아 있던 실습 흔적을 보존하기 위한 자리표시자입니다.
새로운 FastAPI 예제를 추가할 때 아래 순서로 작성하면 됩니다.

1. `app = FastAPI()`로 앱 객체 생성
2. `@app.get(...)` 또는 `@app.post(...)`로 경로 연결
3. 함수에서 dict/list/Pydantic 모델 등을 반환
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping() -> dict[str, str]:
    """서버가 실행 중인지 확인하는 가장 단순한 테스트 엔드포인트."""
    return {"message": "pong"}
