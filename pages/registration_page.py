from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill_email_form(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_user_name_form(self, user_name: str) -> None:
        self.user_name_input.fill(user_name)

    def fill_password_form(self, password: str) -> None:
        self.password_input.fill(password)

    def click_registration_button(self) -> None:
        self.registration_button.click()
