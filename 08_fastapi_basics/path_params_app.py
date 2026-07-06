"""FastAPI 경로 매개변수 실습.

복습 포인트:
- `@app.get("/")`는 기본 주소에 대한 응답을 만든다.
- `/hello/{name}`처럼 중괄호를 쓰면 URL 일부를 함수 인자로 받을 수 있다.

실행:
    uvicorn path_params_app:app --reload
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    """API 서버가 정상 실행 중인지 확인하는 기본 엔드포인트."""
    return {"message": "Welcome to FastAPI!"}


@app.get("/hello/{name}")
def hello(name: str) -> dict[str, str]:
    """URL에 들어온 이름을 받아 맞춤형 인사 메시지를 만든다."""
    return {"message": f"Hello, {name}!"}
