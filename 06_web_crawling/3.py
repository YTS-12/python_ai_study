"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(playwright.sync_api)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
      
  page.goto("https://example.com/")
  print(page.title())

  page_html = page.content()
  print(page_html[:200])
  
  page.wait_for_timeout(5000)
  browser.close()

print('크롤링 완료')