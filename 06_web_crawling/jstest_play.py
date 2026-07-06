"""학습용 스크립트 정리본.
요약: 실습에 필요한 라이브러리나 모듈(playwright.sync_api, time  # 1. time 모듈 추가)을 불러옵니다.
메모: 민감 정보는 환경 변수나 별도 비공개 설정 파일로 분리해 관리하세요.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright
import time  # 1. time 모듈 추가

def run_crawler():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        html_path = Path(__file__).resolve().parents[1] / '99_review_archive' / '03_reference_or_outputs' / '06_web_crawling' / 'jstest.html'
        page.goto(html_path.as_uri())
        page.fill("#nameInput", "파이썬 크롤러")
        page.click("#submitBtn")
        
        result_text = page.inner_text("#resultName")
        print(f"화면에 출력된 이름 : {result_text}")
        
        # ⭐️ 추가된 부분: 결과 확인을 위해 5초간 브라우저 유지
        print("결과 확인을 위해 5초간 대기합니다...")
        time.sleep(5) 
        
        browser.close()

run_crawler()