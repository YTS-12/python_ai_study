"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(openai, os, dotenv)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def msg(role, text):
    msg_src = {"role" : role, "content" : [{"type":"input_text", "text":text}]}
    return msg_src

res = client.responses.create(
    model = 'gpt-4o-mini',
    input = [
        msg("system", "너는 대한민국 기상청이야"),
        msg("user", "오늘과 내일 날씨 알려줘 ")
    ],
    temperature = 0
)
print(res.output_text)