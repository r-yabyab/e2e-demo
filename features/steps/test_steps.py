from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the SauceDemo homepage')
def open_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")

@when('I enter username "{username}"')
def enter_username(context, username):
    wait = WebDriverWait(context.driver, 10)
    username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_input.send_keys(username)

@when('I enter password "{password}"')
def enter_password(context, password):
    wait = WebDriverWait(context.driver, 10)
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.send_keys(password)

@when('I click the login button')
def click_login(context):
    wait = WebDriverWait(context.driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

@then('I should be logged in successfully')
def check_login_success(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))

@then('I should see "{expected_text}" in the login credentials section')
def check_login_credentials(context, expected_text):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "login_credentials")))
    assert expected_text in element.text

def after_scenario(context, scenario):
    context.driver.quit()