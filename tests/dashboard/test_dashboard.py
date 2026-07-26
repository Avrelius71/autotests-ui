import pytest
from pages.dashboard.dashboard_page import DashboardPage
import allure
from config import settings
from tools.epic import AllureEpic
from tools.story import AllureStory
from tools.feature import AllureFeature
from tools.tags import AllureTag
from tools.routes import AppRoute
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Прроверка страницы Дашборд')
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.scores_chart_view.check_visible("Scores")
        dashboard_page_with_state.courses_chart_view.check_visible("Courses")
        dashboard_page_with_state.students_chart_view.check_visible("Students")
        dashboard_page_with_state.activities_chart_view.check_visible("Activities")
