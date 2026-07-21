from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_header_dashboard(self) -> None:
        expect(self.dashboard_header).to_be_visible()
        expect(self.dashboard_header).to_have_text('Dashboard')
