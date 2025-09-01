from selenium import webdriver
# from allure import step


class BaseTest:
    driver = None

    # @step('Инициализировать Веб-драйвер. Открыть браузер')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    # @step('Закрыть браузер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
