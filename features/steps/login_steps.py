from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the SauceDemo homepage')
def open_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")
    context.wait = WebDriverWait(context.driver, 10)

@when('I log in')
def log_in(context):
    context.wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    context.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("secret_sauce")
    context.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

@then('I should see the inventory page')
def check_login_success(context):
    context.wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))

@then('I should see "{expected_text}" in the login credentials section')
def check_login_credentials(context, expected_text):
    context.wait.until(EC.presence_of_element_located((By.ID, "login_credentials")))
    element = context.wait.until(EC.presence_of_element_located((By.ID, "login_credentials")))
    assert expected_text in element.text

@then('I should see a list of users on the homepage')
def check_user_list(context):
    element = context.wait.until(EC.presence_of_element_located((By.ID, "login_credentials")))
    usernames = element.text.splitlines()[1:]
    
    expected_usernames = [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user"
    ]

    assert usernames == expected_usernames, f"Usernames do not match.\nExpected: {expected_usernames}\nFound: {usernames}"

def after_scenario(context, scenario):
    context.driver.quit()