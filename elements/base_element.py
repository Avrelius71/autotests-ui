import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "базовый элемент"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Получить локатор с "data-testid={locator}" по индексу "{nth}"'):  # Добавили шаг
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Нажать на {self.type_of} "{self.name}"'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" видим'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" содержит текст "{text}"'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)
