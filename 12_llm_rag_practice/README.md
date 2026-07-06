# RAG 실습 자료 복습 가이드

이 폴더는 투자보고서 프로젝트와 분리한 학습/실습 자료입니다.

## 1. PDF + FAISS RAG

위치: `01_pdf_faiss_rag`

- `01_pdf_manual_faiss_rag.ipynb`: 삼성카드 매뉴얼 PDF를 로드하고, 청크 분할, OpenAI 임베딩, FAISS 검색, RAG 답변을 실습하는 노트북입니다.
- `simple_rag_pdf_app`: 같은 PDF RAG 흐름을 간단한 앱 코드로 만든 실습 폴더입니다.

복습 순서:

1. PDF 로더가 문서를 `Document` 리스트로 바꾸는 과정
2. `RecursiveCharacterTextSplitter`로 청크를 나누는 과정
3. `FAISS.from_documents()`로 벡터DB를 만드는 과정
4. retriever와 prompt, LLM을 연결하는 과정

## 2. Pinecone RAG

위치: `02_pinecone_rag`

- `01_pinecone_basic_3d_vector_search.ipynb`: Pinecone 기본 벡터 업서트, 필터 검색, fetch, 3D 시각화 실습입니다.
- `02_pinecone_wikipedia_rag.ipynb`: 한국어 Wikipedia 데이터를 넓게 가져와 Pinecone에 임베딩하고 RAG 검색/답변을 실습하는 노트북입니다.
- `99_original_combined_pinecone_experiment.ipynb`: 분리 전 원본 통합 실험 노트북입니다. 참고용으로만 보세요.

복습 순서:

1. `01_pinecone_basic_3d_vector_search.ipynb`
2. `02_pinecone_wikipedia_rag.ipynb`
3. 필요할 때만 `99_original_combined_pinecone_experiment.ipynb`

## 중요 개념

- RAG는 답변 근거가 될 문서가 먼저 임베딩되어 벡터DB에 들어 있어야 합니다.
- `train[:100]`처럼 데이터 범위가 작으면 질문의 답이 들어 있는 문서가 없을 수 있습니다.
- `02_pinecone_wikipedia_rag.ipynb`는 기본값을 `train[:5000]`으로 늘렸고, 필요하면 `WIKI_DATASET_SPLIT`을 더 크게 조정할 수 있습니다.
