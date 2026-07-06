"""FastAPI + CORS + HTML fetch 연결 실습.

복습 포인트:
- CORS 미들웨어는 브라우저에서 다른 출처의 API를 호출할 수 있게 해준다.
- `index.html`의 `fetch("http://127.0.0.1:8000/items/12")`가
  이 파일의 `/items/{item_id}` 엔드포인트와 연결된다.

실행:
    uvicorn main2:app --reload
    그런 다음 index.html을 브라우저에서 열어 버튼을 눌러본다.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# 학습용으로 모든 출처를 허용한다. 실제 서비스에서는 허용할 도메인을 좁혀야 한다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int | str]:
    """상품 ID를 URL에서 받아 샘플 상품 정보를 JSON으로 반환한다."""
    return {"item_id": item_id, "name": "GTX5060"}
