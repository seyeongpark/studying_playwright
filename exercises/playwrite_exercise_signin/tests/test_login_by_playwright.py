# tests/test_login_by_playwright.py
import pytest
from playwright.sync_api import expect
from pages.login_by_playwright import LoginPage

LOGIN_CASES = [
    ("tomsmith", "SuperSecretPassword!", "https://the-internet.herokuapp.com/secure", "You logged into a secure area!"),  # 올바른 자격 증명
    ("invalid_user", "invalid_pass", "https://the-internet.herokuapp.com/login", "Your username is invalid!"),       # username이 잘못된 경우
    ("tomsmith", "wrong_password", "https://the-internet.herokuapp.com/login", "Your password is invalid!"),  # password가 잘못된 경우   
]

@pytest.mark.parametrize("username, password, expected_url, expected_message", LOGIN_CASES)
def test_login_by_playwright(username, password, expected_url, expected_message, page):
    p = LoginPage(page)
    p.open()
    p.login(username, password)
    
    result = p.get_flash_message()
    
    expect(page).to_have_url(expected_url)
    expect(result).to_contain_text(expected_message)

    