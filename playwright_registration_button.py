from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    button = page.get_by_test_id('registration-page-registration-button')
    input_email = page.get_by_test_id('registration-form-email-input').locator('input')
    input_user_name = page.get_by_test_id('registration-form-username-input').locator('input')
    input_password = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(button).to_be_disabled()
    input_email.fill('user.name@gmail.com')
    input_user_name.fill('username')
    input_password.fill('password')
    expect(button).to_be_enabled()

