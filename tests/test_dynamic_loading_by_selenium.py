# tests/test_dynamic_loading_by_selenium.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

def test_dynamic_loading_by_selenium(driver):
    wait = WebDriverWait(driver, 10) # WebDriverWait 객체 생성 (최대 10초 대기)
    
    driver.get(URL) # URL로 이동
    
    # 10초 동안 "Start" 버튼이 클릭 가능해질 때까지 대기하고, 클릭
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))).click() # "Start" 버튼 클릭
    
    word = wait.until(EC.visibility_of_element_located((By.ID, "finish"))) # "Hello World!" 텍스트가 보일 때까지 대기
    assert word.text == "Hello World!" # 텍스트 검증