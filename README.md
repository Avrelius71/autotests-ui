# UI Course Automation Tests

Данный проект содержит автоматизированные тесты для
[тестового приложения UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login).
Тесты написаны с использованием **Python**, **Pytest**, **Allure** и **Playwright**. Исходный код тестового приложения доступен
на [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Обзор проекта

Цель проекта — автоматизировать тестирование приложения UI Course. Автотесты проверяют различные
функциональности приложения, чтобы обеспечить его стабильность и корректность работы.

## Начало работы

### Клонирование репозитория

Для начала работы склонируйте репозиторий проекта с помощью Git:

```bash
git clone https://github.com/Avrelius71/autotests-ui.git
```

### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Следуйте инструкциям
для вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

После активации виртуального окружения установите зависимости проекта из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Дополнительная настройка Playwright (при необходимости)

Если вы запускаете Playwright впервые, может потребоваться установка необходимых браузеров:

```bash
playwright install
```

### Запуск тестов с генерацией Allure-отчёта

Для запуска тестов и генерации Allure-отчёта используйте следующую команду:

```bash
pytest -m "regression" --alluredir=./allure-results
```

Эта команда выполнит все тесты проекта и отобразит результаты в терминале.

### Просмотр Allure-отчёта

После выполнения тестов вы можете сгенерировать и просмотреть Allure-отчёт с помощью команды:

```bash
allure serve allure-results
```

Эта команда откроет Allure-отчёт в браузере по умолчанию.
