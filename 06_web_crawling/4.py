"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(playwright.sync_api, bs4)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

# beautifulsoup 으로 파싱
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto("http://quotes.toscrape.com/")
  
  html = page.content()
  soup = BeautifulSoup(html, 'lxml')
  
  quotes = soup.select('div.quote')  # 리스트로 반환
  quotes_list = []
  
  for quote in quotes:
    quotes_list.append({'quote': quote.select_one('span.text').text,
                       'author': quote.select_one('small.author').text})

  import pandas as pd
  df = pd.DataFrame(quotes_list)
  print(df.head())



