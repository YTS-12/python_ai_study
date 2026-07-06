"""FastAPI GET/POST 기초 실습.

복습 포인트:
- GET은 서버의 데이터를 조회할 때 사용한다.
- POST는 클라이언트가 보낸 데이터를 서버가 받아 처리할 때 사용한다.

실행:
    uvicorn get_post_basic:app --reload
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def say_hello() -> dict[str, str]:
    """브라우저나 클라이언트에서 GET 요청을 보내면 간단한 JSON을 반환한다."""
    return {"message": "안녕하세요"}


@app.post("/echo")
def echo(data: dict) -> dict[str, dict]:
    """요청 본문으로 들어온 JSON 데이터를 그대로 다시 돌려준다."""
    return {"received_data": data}
