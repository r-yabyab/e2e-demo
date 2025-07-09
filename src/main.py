import pytest
from playwright.sync_api import sync_playwright, Playwright

WEB_URL = "https://www.saucedemo.com"

@pytest.fixture(scope="session")
def setup_browser():
    print("Launching Playwright...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    yield page

    print("Closing browser...")
    browser.close()
    playwright.stop()


def test_grab_content(setup_browser):
    page = setup_browser
    page.wait_for_selector("#login_credentials")
    content = page.locator("#login_credentials").inner_text()
    print("Content:", content)
    assert "standard_user" in content, "Expected login credentials not found!"


def test_login(setup_browser):
    page = setup_browser
    page.wait_for_selector("#user-name").type("standard_user")
    page.wait_for_selector("#password").type("secret_sauce")
    page.wait_for_selector("#login-button").click()

    page.wait_for_selector("#menu_button_container > div > div:nth-child(1) > div").click()

    content = page.locator("#logout_sidebar_link").inner_text()
    assert "Logout" in content, "Expected logout link not found!"

    page.wait_for_selector("#logout_sidebar_link").click()

    logged_out = page.locator("#login_credentials").inner_text()
    assert "standard_user" in logged_out, "Expected login credentials not found after logout!"