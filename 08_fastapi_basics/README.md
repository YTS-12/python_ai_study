# FastAPI 기초 실습

루트에 흩어져 있던 FastAPI 입문 파일을 모은 폴더입니다.

## 복습 순서

1. `exam1.py`: 가장 작은 FastAPI 앱 구조
2. `path_params_app.py` 또는 `main.py`: 경로 매개변수 연습
3. `get_post_basic.py`: GET/POST 차이 연습
4. `exam2.py`: 응답 타입, 경로/쿼리 매개변수, Pydantic body 종합 연습
5. `main2.py` + `index.html`: 브라우저 fetch와 CORS 연결 확인
6. `exam3.py`: 새 예제를 추가하기 위한 자리표시자

## 실행 예시

```powershell
uvicorn exam2:app --reload
```

브라우저에서 `http://127.0.0.1:8000/docs`를 열면 Swagger UI로 GET/POST 요청을 직접 테스트할 수 있습니다.
