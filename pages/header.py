from selenium.webdriver.common.by import By
from allure import step

from pages.base_page import BasePage


class Header(BasePage):
    yandex_logo = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]'
    scooter_logo = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]'

    @step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self) -> None:
        self.click(self.yandex_logo)

    @step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self) -> None:
        self.click(self.scooter_logo)
