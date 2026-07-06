# data-science-study

파이썬부터 데이터 분석, 머신러닝/딥러닝, LLM까지 공부하면서 작성한 실습 노트북 모음입니다.
주제별로 폴더를 나눠 정리해 두었습니다.

## 폴더 구성

| 폴더 | 내용 |
|---|---|
| `01_python_basics` | 파이썬 문법 기초 (변수, 자료형, 조건문, 반복문, 함수, 클래스) |
| `02_sql_database` | SQL 기초와 MySQL 연결 (SELECT, JOIN, 함수, 서브쿼리) |
| `03_statistics_data_analysis` | 통계, pandas, 시각화, EDA, 전처리 |
| `04_prompt_engineering_llm` | OpenAI API 프롬프트 엔지니어링 |
| `05_machine_learning` | scikit-learn 분류/회귀/군집 모델링 |
| `06_web_crawling` | requests, BeautifulSoup 크롤링 |
| `07_streamlit_apps` | Streamlit 기초 앱 |
| `08_fastapi_basics` | FastAPI 기초 (라우팅, 요청/응답) |
| `10_reports` | 데이터 분석 보고서 (통신사 고객 이탈) |
| `11_deep_learning_practice` | HuggingFace NLP, YOLO 객체탐지 |
| `12_llm_rag_practice` | FAISS / Pinecone 기반 RAG 실습 |
| `90_shared_data_assets` | 여러 노트북에서 공통으로 쓰는 데이터셋 |

## 실행

대부분 Jupyter Notebook이고 일부는 Python 스크립트입니다.

```bash
pip install -r requirements.txt   # 폴더별로 필요한 패키지가 다릅니다
jupyter lab
```

API 키가 필요한 실습(프롬프트 엔지니어링, RAG 등)은 각 폴더에 `.env`를 만들고 키를 넣어야 동작합니다.
`.env`는 저장소에 올리지 않으며, 필요한 키 목록은 `.env.example`을 참고하면 됩니다.

## 참고

- API 키·DB 비밀번호 같은 민감 정보는 코드에서 분리해 `os.getenv()` / `.env` 로 관리합니다.
- 데이터는 공개 데이터셋 위주이며, 일부 실습 결과물도 함께 두었습니다.
