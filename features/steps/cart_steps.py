from behave import given, when, then
from playwright.sync_api import sync_playwright

@given("I log in with Playwright")
def step_log_in(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com")
    context.page.fill('#user-name', 'standard_user')
    context.page.fill('#password', 'secret_sauce')
    context.page.wait_for_selector('#login-button').click()

@when("I go to the inventory page")
def step_go_to_inventory_page(context):
    context.page.wait_for_selector("#inventory_container")

@when('I add a backpack to the cart')
def step_add_backpack_to_cart(context):
    context.page.wait_for_selector("#add-to-cart-sauce-labs-backpack")
    context.page.click("#add-to-cart-sauce-labs-backpack")


@then('the cart icon should show "{count}"')
def step_cart_should_show(context, count):
    badge = context.page.wait_for_selector(".shopping_cart_badge")
    actual = badge.inner_text()
    assert actual == count, f"Expected cart to show {count}, but got {actual}"

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()
