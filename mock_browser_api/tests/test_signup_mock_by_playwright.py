# tests/test_signup_mock_by_playwright.py

from playwright.sync_api import expect, sync_playwright
from pages.signup_by_playwright import SignupPage
import json, pytest

URL = "file:///C:/Users/EDU01-06/Documents/swtest/swtest_playwrite/mock/pages/signup_mock.html"

FAKE_CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status": "ok", "message": "회원가입 성공(Mocked)", "expected_msg": "회원가입 성공(Mocked)"}
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status": "error", "message": "서버 오류 발생!!", "expected_msg": "서버 오류 발생!!"}
    },
]

@pytest.mark.parametrize("case", FAKE_CASES, ids=[case["id"] for case in FAKE_CASES])
def test_signup(page, case):
    def handle_mock_response(route):
        route.fulfill(
            status=case["status"],
            content_type="application/json",
            body=json.dumps(case["json_body"])
        )
    
    # 페이지의 API 요청을 가로채서 모킹 응답을 반환하도록 설정
    page.route("http://localhost:8000/api/signup", handle_mock_response)
    
    sp = SignupPage(page)
    sp.open(URL)
    sp.signup(
        email="user@example.com",
        username="tester",
        password="abc12345",
        confirm="abc12345",
        terms=True
    )
    
    print("Mock Test Message:", sp.get_flash_msg())
    expect(sp.flash).to_contain_text(case["json_body"]["expected_msg"])