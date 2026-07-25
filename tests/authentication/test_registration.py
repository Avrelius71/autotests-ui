import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.epic import AllureEpic
from tools.story import AllureStory
from tools.feature import AllureFeature
from tools.tags import AllureTag
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Регистрация с валидными данными')
    def test_successful_registration(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage
    ):
        registration_page.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        )
        registration_page.registration_form.fill('test@ya.ru', 'test', 'password123')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
