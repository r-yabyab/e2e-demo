# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# WEB_URL = "https://www.saucedemo.com"

# @pytest.fixture(scope="session")
# def setup_browser():
#     print("Launching Selenium Chrome browser...")

#     options = Options()
#     options.headless = False  # Set True to run headless

#     driver = webdriver.Chrome(options=options)
#     driver.get(WEB_URL)

#     yield driver

#     print("Closing browser...")
#     driver.quit()


# def test_grab_content(setup_browser):
#     driver = setup_browser
#     wait = WebDriverWait(driver, 10)

#     # Wait for the element with id 'login_credentials'
#     login_cred_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_credentials")))
#     content = login_cred_elem.text
#     print("Content:", content)
#     assert "standard_user" in content, "Expected login credentials not found!"


# def test_login(setup_browser):
#     driver = setup_browser
#     wait = WebDriverWait(driver, 10)

#     # Fill username
#     username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
#     username_input.send_keys("standard_user")

#     # Fill password
#     password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
#     password_input.send_keys("secret_sauce")

#     # Click login button
#     login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
#     login_button.click()

#     # Click menu button using same selector as Playwright
#     menu_button = wait.until(EC.element_to_be_clickable(
#         (By.CSS_SELECTOR, "#menu_button_container > div > div:nth-child(1) > div")
#     ))
#     menu_button.click()

#     # Check logout link text
#     logout_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logout_sidebar_link")))
#     content = logout_link.text
#     assert "Logout" in content, "Expected logout link not found!"

#     # Click logout
#     logout_link.click()

#     # After logout, wait for login credentials visible again
#     login_cred_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_credentials")))
#     logged_out_content = login_cred_elem.text
#     assert "standard_user" in logged_out_content, "Expected login credentials not found after logout!"
