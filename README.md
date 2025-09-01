# Проект автоматизации тестирования системы Яндекс.Самокат
## 1. Используемые фрейворки
* pytest
* Selenium
* allure-pytest
## 2. Установка
Установить зависимости: `pip install -r requirements.txt`
## 3. Запуск
Команда для запуска тестов: `pytest --alluredir=allure_results`
## 4. Отчет о тестировании
Команда генерации отчета Allure: `allure serve allure_results`
