# playwright/2.webpage_open.py

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 브라우저 실행
    context = browser.new_context()  # 새로운 브라우저 컨텍스트 생성
    
    page = context.new_page()
    page.goto("https://google.com")             # 사이트 이동
    print(page.title())                          # 페이지 제목 출력
    page.screenshot(path="screenshot.png")          # 스크린샷 저장

    page.pause()  # 브라우저 일시 정지 (개발자 도구에서 계속 진행 가능)
    context.close()
    browser.close()