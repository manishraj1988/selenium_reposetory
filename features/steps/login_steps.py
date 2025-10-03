from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage

@given('I am on the login page')
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()

@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when('I click the login button')
def step_click_login(context):
    context.login_page.click_login_button()

@when('I login with username "{username}" and password "{password}"')
def step_login_with_credentials(context, username, password):
    context.login_page.login(username, password)

@then('I should see the error message')
def step_verify_error_displayed(context):
    assert context.login_page.is_error_displayed(), "Error message not displayed"

@then('the error message should contain "{text}"')
def step_verify_error_text(context, text):
    error_message = context.login_page.get_error_message()
    assert text.lower() in error_message.lower(), \
        f"Expected '{text}' in error message, but got '{error_message}'"

@then('I should be redirected to the home page')
def step_verify_home_page(context):
    context.home_page = HomePage(context.driver)
    current_url = context.driver.current_url
    assert "home" in current_url or "dashboard" in current_url, \
        f"Expected home/dashboard in URL, but got {current_url}"

@then('I should see the welcome message')
def step_verify_welcome_message(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.is_logged_in(), "User is not logged in"