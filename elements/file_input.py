import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "поле загрузки файла"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Установить файл "{file}" в {self.type_of} "{self.name}"'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
