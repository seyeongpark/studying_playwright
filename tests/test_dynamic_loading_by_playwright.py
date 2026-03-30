# tests/test_dynamic_loading_by_playwright.py

from playwright.sync_api import expect, sync_playwright, Page

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

def test_dynamic_loading_by_playwright(page: Page):
    page.goto(URL) # URL로 이동
    
    # 10초 동안 "Start" 버튼이 클릭 가능해질 때까지 대기하고, 클릭
    page.locator("#start button").click() # "Start" 버튼 클릭
    
    flash_msg = page.locator("#finish") # "Hello World!" 텍스트가 보일 때까지 대기

    expect(flash_msg).to_have_text("Hello World!", timeout=10000) # 텍스트 검증
    # assert flash_msg.text_content() == "Hello World!" # 텍스트 검증