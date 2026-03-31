# playwright/3.multi_pages.py

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 브라우저 실행

    page1 =browser.new_page()
    page1.goto("https://google.com")             # 사이트 이동
    print(page1.title())                          # 페이지 제목 출력
    
    page2 = browser.new_page()
    page2.goto("https://naver.com")              # 사이트 이동
    print(page2.title())                          # 페이지 제목 출력

    input("Press Enter to close the browser...")  # 사용자 입력 대기    
    browser.close()