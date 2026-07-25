import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
import allure


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step("Проверить видимость боковой панели")
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step("Нажать «Выход» на боковой панели")
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Нажать «Курсы» на боковой панели")
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step("Нажать «Дашборд» на боковой панели")
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))
