# tests/test_subscribe_email_by_playwright.py
import pytest
from playwright.sync_api import expect
from exercises.playwrite_exercise_self.pages.subscribe_email_by_playwright import SubscribeEmailPage

SUBSCRIBE_CASES = [
    # 유효한 이메일과 주제로 구독 시도
    ("test@example.com", "Testing & QA", "Subscribed to qa updatesefefefe"),
    ("test@example.com", "Frontend patterns", "Subscribed to frontend updates"),
    ("test@example.com", "Automation drills", "Subscribed to automation updates"), 
    
    # 유효하지 않은 이메일로 구독 시도
    ("invalid-email", "Testing & QA", "Enter a valid email"),
    ("", "Testing & QA", "Enter a valid email"),
    ("invalid@examplecom", "Testing & QA", "Enter a valid email"),
    
    # 주제를 선택하지 않고 구독 시도
    ("test@example.com", "", "Pick a topic"),
]

@pytest.mark.parametrize("email, topic, expected_message", SUBSCRIBE_CASES)
def test_subscribe_by_playwright(email, topic, expected_message, page):
    p = SubscribeEmailPage(page)
    p.open()
    p.subscribe(email, topic)
    
    result = p.get_flash_message()
    
    expect(result).to_contain_text(expected_message)

    