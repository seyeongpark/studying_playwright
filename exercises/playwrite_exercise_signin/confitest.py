import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# headless 옵션 등록
def pytest_addoption(parser):
    parser.addoption("--headless", action = "store_true", default = False)


# 웹페이지 selenium 크롬 드라이버
@pytest.fixture(scope="function")
def driver(request):
    print("Setting up WebDriver...")
    headless = request.config.getoption("--headless") # headless 가 있는지 보는 것
    # headless = “브라우저를 눈에 안 보이게 실행하는 모드”
    
    opts = Options()
    if headless:
        opts.add_argument("--headless==new")
        opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    
    yield driver # 테스트 함수에게 전달 할 수 있음
    driver.quit() # 테스트 함수가 끝나면 드라이버 종료
    
@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.delete_all_cookies()
    driver.get("about:blank")
    
    # playwright
from playwright.sync_api import sync_playwright
# 브라우저는 한 번만 띄우고
@pytest.fixture(scope="session")
def browser(request):
    headless = request.config.getoption("--headless")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

# 각 테스트(케이스)마다 깨끗한 세션/탭 사용
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()