import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def build_pdf_path() -> str:
    """
    현재 파일(rag_chain.py) 위치를 기준으로
    data/Samsung_Card_Manual_Korean_1.3.pdf 경로를 생성합니다.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(
        base_dir,
        "data",
        "Samsung_Card_Manual_Korean_1.3.pdf"
    )
    return pdf_path


def load_rag_chain(
    pdf_path: str | None = None,
    model: str = "gpt-4o-mini",
    embedding_model: str = "text-embedding-3-small"
):
    """
    PDF 기반 RAG 체인을 생성합니다.

    Args:
        pdf_path: PDF 파일 경로. None이면 기본 경로 자동 설정
        model: 답변 생성용 OpenAI 채팅 모델
        embedding_model: 임베딩 모델명

    Returns:
        rag_chain: 질문 -> 검색 -> 프롬프트 -> LLM -> 문자열 응답 체인
    """
    load_dotenv()

    if pdf_path is None:
        pdf_path = build_pdf_path()

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"PDF 파일을 찾을 수 없습니다.\n확인한 경로: {pdf_path}"
        )

    # 1. PDF 로드
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # 2. 텍스트 분할
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    docs = splitter.split_documents(pages)

    # 3. 임베딩 + 벡터 DB
    embeddings = OpenAIEmbeddings(model=embedding_model)
    vectordb = FAISS.from_documents(docs, embeddings)

    # 4. Retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # 5. 프롬프트
    prompt = ChatPromptTemplate.from_template("""
너는 삼성 메모리카드 매뉴얼 전문 어시스턴트이다.
반드시 아래 참고 문서를 근거로만 답변하라.
참고 문서에 없는 내용은 추측하지 말고, 문서에서 확인되지 않는다고 답하라.

[참고문서]
{context}

[질문]
{question}

한글로 간결하고 정확하게 답변하라.
""".strip())

    # 6. LLM
    llm = ChatOpenAI(
        model=model,
        temperature=0
    )

    # 7. RAG 체인
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain