import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def setup_browser():
    print("Launching Selenium Chrome browser...")
    chrome_options = Options()
    service = ChromeService()
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.saucedemo.com")
    yield driver

    print("Closing browser...")
    driver.quit()


def test_grab_content(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "login_credentials")))
    content = element.text
    print("Content:", content)
    assert "standard_user" in content, "Expected login credentials not found!"


def test_login(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_input.send_keys("standard_user")
    
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.send_keys("secret_sauce")
    
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
