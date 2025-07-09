# from behave import given, when, then
# from playwright.sync_api import sync_playwright

# @given("I open the SauceDemo homepage with Playwright")
# def step_open_homepage(context):
#     context.playwright = sync_playwright().start()
#     context.browser = context.playwright.chromium.launch(headless=False)
#     context.page = context.browser.new_page()
#     context.page.goto("https://www.saucedemo.com")

# @when('I input username "{username}"')
# def step_input_username(context, username):
#     context.page.fill('#user-name', username)

# @when('I input password "{password}"')
# def step_input_password(context, password):
#     context.page.fill('#password', password)
#     context.page.click('#login-button')

# @when("I click the login button with Playwright")
# def step_click_login_pw(context):
#     context.page.wait_for_selector("#login-button").click()
#     context.page.wait_for_selector("#inventory_container")

# @when('I click the element with selector "{selector}"')
# def step_click_selector(context, selector):
#     context.page.wait_for_selector(selector).click()

# @then('the cart should show "{count}"')
# def step_cart_should_show(context, count):
#     badge = context.page.wait_for_selector(".shopping_cart_badge")
#     actual = badge.inner_text()
#     assert actual == count, f"Expected cart to show {count}, but got {actual}"

# def after_scenario(context, scenario):
#     context.browser.close()
#     context.playwright.stop()
