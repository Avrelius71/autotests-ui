from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Открыть URL "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        step = f'Перезагрузить страницу с URL "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Проверить, что текущий URL соответствует шаблону "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
