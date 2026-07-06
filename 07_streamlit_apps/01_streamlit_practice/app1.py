"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(streamlit as st)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

from pathlib import Path

import streamlit as st

st.title('안녕하세요')

#브라우저에 텍스트 출력
st.write('hello streamlit!!!')
st.divider()

name = st.text_input ( '이름 : ')

st.write(name)\

def bt1_click():
  st.write('그렇구나... 잘했어...')


st.write('')
# btn1 = st.button('눌러봐', on_click = bt1_click)
btn1 = st.button('눌러봐')
if btn1 :
  #st.write('정말 눌렀어??')
  bt1_click()


import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / 'pew.csv'
df = pd.read_csv(DATA_PATH)

#log 출력하기
print(df.info())


st.write(df.head())
