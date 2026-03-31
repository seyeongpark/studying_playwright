# pages/login_by_playwright.py

from playwright.sync_api import Page

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")
        
    def open(self):
        self.page.goto(self.URL)
        
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def logout(self):
        self.logout_button.click()
        
    def get_flash_message(self):
        self.flash_message.wait_for()  # 메시지가 나타날 때까지 대기
        return self.flash_message


# LoginPage 클래스 동작 확인 코드 작성
if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # 브라우저 창을 띄우기 위해 headless=False로 설정
        page = browser.new_page()
        
        login = LoginPage(page)
        login.open()
        
        # 로그인 시도
        login.login("tomsmith", "SuperSecretPassword!")
        print("Flash Message after login:", login.get_flash_message())
        # 로그아웃 시도
        login.logout()
        print("Flash Message after logout:", login.get_flash_message())
        browser.close()