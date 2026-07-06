import os
import streamlit as st

from rag_chain import load_rag_chain, build_pdf_path

# -----------------------------------------------
# 페이지 설정
# -----------------------------------------------
st.set_page_config(
    page_title="삼성 메모리카드 매뉴얼 챗봇",
    page_icon="📖",
    layout="centered"
)

st.title("삼성 메모리카드 매뉴얼 챗봇")
st.caption("매뉴얼 기반으로 정확한 답변을 제공합니다.")

# -----------------------------------------------
# PDF 경로 설정
# -----------------------------------------------
PDF_PATH = build_pdf_path()

# 경로 확인용
with st.expander("현재 PDF 경로 확인", expanded=False):
    st.code(PDF_PATH)

# -----------------------------------------------
# RAG 체인 초기화 (최초 1회만 실행)
# -----------------------------------------------
@st.cache_resource
def get_chain():
    return load_rag_chain(pdf_path=PDF_PATH)

try:
    rag_chain = get_chain()
except Exception as e:
    st.error(f"RAG 체인 초기화 중 오류가 발생했습니다:\n{e}")
    st.stop()

# -----------------------------------------------
# 대화 히스토리 초기화
# -----------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "질문을 입력하면 매뉴얼 내용을 바탕으로 답변합니다."
        }
    ]

# -----------------------------------------------
# 이전 대화 출력
# -----------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------------------
# 사용자 입력 처리
# -----------------------------------------------
user_input = st.chat_input("예: 이 유틸리티는 동시에 몇 개의 메모리카드나 UFD를 인식하나요?")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("매뉴얼을 검색해 답변 생성 중..."):
            try:
                answer = rag_chain.invoke(user_input)
            except Exception as e:
                answer = f"답변 생성 중 오류가 발생했습니다:\n{e}"

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })