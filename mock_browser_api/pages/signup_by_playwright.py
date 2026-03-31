# pages/signup_by_playwright.py

from playwright.sync_api import Page


class SignupPage:
    URL = "file:///C:/Users/EDU01-06/Documents/swtest/swtest_playwrite/mock/signup.html"
    
    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.locator("#email")
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.confirm_input = page.locator("#confirm")
        self.terms_checkbox = page.locator("#terms")
        self.submit_button = page.locator('button[type="submit"]')

        self.flash = page.locator("#flash")

    def open(self, url = URL):
        self.page.goto(url)

    def signup(self, email="", username="", password="", confirm="", terms=False):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_input.fill(confirm)

        if terms:
            self.terms_checkbox.check()
        else:
            self.terms_checkbox.uncheck()

        self.submit_button.click()

    def get_flash_msg(self) -> str:
        return self.flash.text_content()
    

if __name__ == "__main__":

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        signup_page = SignupPage(page)

        signup_page.open()
        signup_page.signup(            
            email="user@example.com",
            username="tester",
            password="abc12345",
            confirm="abc12345",
            terms=True)
        
        print(signup_page.get_flash_msg())

        browser.close()