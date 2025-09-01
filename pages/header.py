from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):
    yandex_logo = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]'
    scooter_logo = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]'

    def click_yandex_logo(self) -> None:
        self.click(self.yandex_logo)

    def click_scooter_logo(self) -> None:
        self.click(self.scooter_logo)
