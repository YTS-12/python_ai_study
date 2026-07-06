"""가장 작은 FastAPI 서버 예제.

복습 포인트:
- `FastAPI()` 객체가 애플리케이션의 중심이다.
- 데코레이터(`@app.get`)로 URL과 함수를 연결한다.

실행:
    uvicorn exam1:app --reload
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """루트 경로로 접속하면 서버 상태 확인용 메시지를 반환한다."""
    return {"message": "Hello, FastAPI"}
