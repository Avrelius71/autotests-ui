from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Открыть URL "{url}"'): # Добавили allure.step
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Перезагрузить страницу с URL "{self.page.url}"'): # Добавили allure.step
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Проверить, что текущий URL соответствует шаблону "{expected_url.pattern}"'): # Добавили allure.step
            expect(self.page).to_have_url(expected_url)
