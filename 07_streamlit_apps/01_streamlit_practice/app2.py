"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(random, datetime, streamlit as st)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

import random
from datetime import datetime

import streamlit as st

# ----------------------------
# 0) 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="환경 상태 미니 대시보드",
    page_icon="🌿",
    layout="wide"
)

st.title("환경 상태 미니 대시보드")
st.caption("온도(°C)와 공기질(AQI)을 2개의 metric 카드로 표시합니다. 버튼을 누르면 값이 갱신되고 변화량(Δ)에 따라 색상이 자동으로 바뀝니다.")
st.divider()

# ----------------------------
# 1) 세션 상태 초기화 (이전/현재 값 보관)
# ----------------------------
if "temp_prev" not in st.session_state:
    st.session_state.temp_prev = 23.0
if "temp_curr" not in st.session_state:
    st.session_state.temp_curr = 23.0

if "aqi_prev" not in st.session_state:
    st.session_state.aqi_prev = 55
if "aqi_curr" not in st.session_state:
    st.session_state.aqi_curr = 55

if "last_updated" not in st.session_state:
    st.session_state.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------------------
# 2) 값 갱신 로직
# ----------------------------
def refresh_values():
    # 이전값 저장
    st.session_state.temp_prev = st.session_state.temp_curr
    st.session_state.aqi_prev = st.session_state.aqi_curr

    # 현재값 업데이트(예시: 랜덤 변동)
    st.session_state.temp_curr = round(st.session_state.temp_curr + random.uniform(-1.2, 1.2), 1)
    st.session_state.aqi_curr = int(max(0, st.session_state.aqi_curr + random.randint(-12, 12)))

    st.session_state.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------------------
# 3) 컨트롤(버튼)
# ----------------------------
col_btn1, col_btn2, _ = st.columns([1, 1, 6])
with col_btn1:
    st.button("값 갱신", on_click=refresh_values)
with col_btn2:
    st.write(f"업데이트: {st.session_state.last_updated}")

st.divider()

# ----------------------------
# 4) 메트릭 카드 2개(가로 배치)
# ----------------------------
c1, c2 = st.columns(2)

temp_delta = st.session_state.temp_curr - st.session_state.temp_prev
aqi_delta = st.session_state.aqi_curr - st.session_state.aqi_prev

with c1:
    st.metric(
        label="온도 (°C)",
        value=f"{st.session_state.temp_curr:.1f}",
        delta=f"{temp_delta:+.1f} °C",
        delta_color="normal",  # 증가=초록, 감소=빨강
    )

with c2:
    st.metric(
        label="공기질 (AQI, 낮을수록 좋음)",
        value=f"{st.session_state.aqi_curr:d}",
        delta=f"{aqi_delta:+d} AQI",
        delta_color="inverse",  # 증가=빨강(악화), 감소=초록(개선)
    )

# ----------------------------
# (선택) 참고 정보
# ----------------------------
st.caption(
    "해석 예시: 공기질(AQI)은 값이 올라가면 악화로 보는 경우가 많아, delta_color='inverse'를 사용했습니다."
)
