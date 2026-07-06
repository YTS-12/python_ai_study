"""FastAPI 기본 라우팅 복습 파일.

`02_app.py`와 거의 같은 구조이며, 경로 매개변수 이름만 `ts`로 바꾸어
URL 값이 함수 인자로 연결되는 방식을 반복 연습한다.

실행:
    uvicorn main:app --reload
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    """루트 경로(`/`) 요청에 대한 기본 응답."""
    return {"message": "Welcome to FastAPI!"}


@app.get("/hello/{ts}")
def hello(ts: str) -> dict[str, str]:
    """URL의 `{ts}` 부분을 문자열로 받아 응답 메시지에 넣는다."""
    return {"message": f"Hello, {ts}!"}
