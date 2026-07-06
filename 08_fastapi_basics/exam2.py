"""FastAPI 응답 타입, 경로/쿼리 매개변수, POST body 종합 실습.

복습 포인트:
- GET 엔드포인트는 dict, list, 문자열, 숫자 등 다양한 값을 JSON 응답으로 바꿔준다.
- `/items/{item_id}` 같은 경로 매개변수와 `?discount=true` 같은 쿼리 매개변수를 함께 받을 수 있다.
- Pydantic `BaseModel`을 쓰면 POST 요청 body의 구조를 명확하게 정의할 수 있다.

실행:
    uvicorn exam2:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    """상품 등록 POST 요청에서 받을 데이터 구조."""

    name: str
    price: int


class User(BaseModel):
    """사용자 등록 POST 요청에서 받을 데이터 구조."""

    username: str
    age: int


@app.get("/test1")
async def root1() -> dict[str, str]:
    """dict를 반환하면 FastAPI가 JSON 객체로 변환한다."""
    return {"name": "하리"}


@app.get("/test2")
async def root2() -> list[str]:
    """list를 반환하면 JSON 배열로 변환된다."""
    return ["하리", "망치", "겨울"]


@app.get("/test3")
async def root3() -> str:
    """문자열은 JSON 문자열로 반환된다. HTML 렌더링은 별도 Response가 필요하다."""
    return "<h1>안녕</h1>"


@app.get("/test4")
async def root4() -> int:
    """숫자도 JSON 숫자로 반환된다."""
    return 1000


@app.get("/users/count")
async def get_user_count() -> int:
    """사용자 수처럼 단일 값을 반환하는 API 예시."""
    return 1523


@app.get("/items/sample")
async def read_sample_item() -> dict[str, str]:
    """고정된 샘플 경로는 동적 경로보다 위에 두면 충돌을 피하기 쉽다."""
    return {"item_id": "sample"}


@app.get("/items/{item_id}")
def get_item(item_id: int, discount: bool = False) -> dict[str, int | bool]:
    """경로 매개변수 `item_id`와 쿼리 매개변수 `discount`를 함께 받는다."""
    return {"item_id": item_id, "discount": discount}


@app.get("/items/{item_id}/orders/{order_id}")
def get_order(item_id: int, order_id: int) -> dict[str, int]:
    """중첩 경로에서 상품 ID와 주문 ID를 동시에 받는다."""
    return {"item_id": item_id, "order_id": order_id}


@app.get("/stocks/{ticker}/history")
def get_stock_history(ticker: str, days: int, market: str) -> dict[str, str | int]:
    """주식 티커는 경로로, 조회 기간과 시장은 쿼리로 받는 API 예시."""
    return {
        "ticker": ticker,
        "days": days,
        "market": market,
        "message": "주가 이력 조회 성공",
    }


@app.post("/items")
def create_item(item: Item) -> dict[str, int | str]:
    """Pydantic 모델로 받은 상품 정보를 응답에 다시 담아 확인한다."""
    return {
        "name": item.name,
        "price": item.price,
        "message": "상품 등록 완료",
    }


@app.post("/users")
def create_user(user: User) -> dict[str, int | str]:
    """Pydantic 모델로 받은 사용자 정보를 응답에 다시 담아 확인한다."""
    return {
        "username": user.username,
        "age": user.age,
        "message": "사용자 등록 완료",
    }
