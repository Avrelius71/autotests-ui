import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "кнопка"

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" активна'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" неактивна'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()
