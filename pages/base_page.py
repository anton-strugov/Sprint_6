from typing import List, Tuple

from selenium.webdriver.support.wait import WebDriverWait as wd_wait
from selenium.webdriver.support import expected_conditions as exp_conds
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from allure import step

from config import Config


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @step('Найти элемент по локатору')
    def find_element(
        self,
        locator: Tuple[str, str],
        template_value: str = None,
    ) -> WebElement:
        if template_value is not None:
            new_locator = locator[1].format(template_value)
            return self.driver.find_element(locator[0], new_locator)
        return self.driver.find_element(*locator)

    @step('Найти список элементов по локатору')
    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    @step('Кликнуть по элементу')
    def click(self, locator: Tuple[str, str]) -> None:
        self.find_element(locator).click()

    @step('Установить текст элемента')
    def set_text(self, locator: Tuple[str, str], *values: str) -> None:
        element = self.find_element(locator)
        for value in values:
            element.send_keys(value)

    @step('Ожидать перехода на указанный url')
    def wait_until_url_to_be(
        self,
        url: str,
        timeout: int = Config.TIMEOUT,
    ) -> None:
        wd_wait(self.driver, timeout).until(
            exp_conds.url_to_be(url),
        )

    @step('Проверить, что url равен указанному')
    def is_url_equal(self, url: str, timeout: int = Config.TIMEOUT) -> bool:
        try:
            self.wait_until_url_to_be(url, timeout)
        except TimeoutError:
            return False
        return True

    @step('Ожидать появления указанного элемента')
    def wait_until_element_visible(
        self,
        target: Tuple[str, str] | WebElement,
        timeout: int = Config.TIMEOUT,
    ) -> None:
        if not isinstance(target, WebElement):
            target = self.find_element(target)
        wd_wait(self.driver, timeout).until(
            exp_conds.visibility_of(target),
        )

    @step('Проверить видимость указанного элемента')
    def is_element_visible(
        self,
        locator: Tuple[str, str],
        timeout: int = Config.TIMEOUT,
    ) -> bool:
        try:
            self.wait_until_element_visible(locator, timeout)
        except TimeoutError:
            return False
        return True

    @step('Прокрутить страницу к элементу')
    def scroll_to_element(self, target: WebElement) -> None:
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);',
            target,
        )

    @step('Получить количество открытых вкладок')
    def get_tabs_count(self) -> int:
        return len(self.driver.window_handles)

    @step('Переключиться на новую вкладку')
    def switch_to_new_tab(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])
