# tests/test_dynamic_loading_by_playwright.py

from playwright.sync_api import expect, sync_playwright, Page

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

def test_dynamic_loading_by_playwright(page: Page):
    page.goto(URL) # URL로 이동
    
    # 10초 동안 "Start" 버튼이 클릭 가능해질 때까지 대기하고, 클릭
    page.locator("#start button").click() # "Start" 버튼 클릭
    
    flash_msg = page.locator("#finish").inner_text() # "Hello World!" 텍스트가 나타날 때까지 대기 후 텍스트 가져오기

    assert "Hello World!" in flash_msg # "Hello World!" 텍스트가 flash_msg에 포함되어 있는지 확인
    