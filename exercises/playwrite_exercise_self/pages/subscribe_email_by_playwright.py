# pages/subscribe_email_by_playwright.py

from playwright.sync_api import Page
import time
class SubscribeEmailPage:
    URL = "https://autotestsandbox.com/examples/newsletter-subscribe-form"
    
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[type='email']")
        self.topic_list = page.locator("data-test-id=newsletter-subscribe-form-secondary")
        self.subscribe_button = page.locator("data-test-id=newsletter-subscribe-form-action")
        self.flash_message = page.locator("data-test-id=newsletter-subscribe-form-message")
        
    def open(self):
        self.page.goto(self.URL)
        
    def subscribe(self, email: str, topic: str):
        self.email_input.fill(email)
        self.topic_list.select_option(topic)
        self.subscribe_button.click()
        
    def get_flash_message(self):
        self.flash_message.wait_for() 
        return self.flash_message


# SubscribeEmailPage 클래스 동작 확인 코드 작성
if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # 브라우저 창을 띄우기 위해 headless=False로 설정
        page = browser.new_page()
        
        subscribe_email = SubscribeEmailPage(page)
        subscribe_email.open()
        
        # 이메일 구독 시도
        subscribe_email.subscribe("test@example.com", "Testing & QA")
        print("Flash Message after subscription:", subscribe_email.get_flash_message())
        
        time.sleep(5)  # 결과 확인을 위해 잠시 대기
        browser.close()