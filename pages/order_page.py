from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from allure import step

from pages.base_page import BasePage


class OrderPage(BasePage):
    first_name_input = By.XPATH, './/input[contains(@placeholder, "Имя")]'
    last_name_input = By.XPATH, './/input[contains(@placeholder, "Фамилия")]'
    address_input = By.XPATH, './/input[contains(@placeholder, "Адрес")]'
    metro_station_input = (
        By.XPATH,
        './/input[contains(@placeholder, "Станция метро")]',
    )
    phone_input = By.XPATH, './/input[contains(@placeholder, "Телефон")]'
    date_input = (
        By.XPATH,
        './/input[contains(@placeholder, "Когда привезти самокат")]',
    )
    rental_period_field = (
        By.XPATH,
        './/div[contains(text(), "Срок аренды")]',
    )
    color_group = By.XPATH, './/div[text()="Цвет самоката"]'
    comment_input = (
        By.XPATH,
        './/input[@placeholder="Комментарий для курьера"]',
    )
    next_btn = By.XPATH, './/button[text()="Далее"]'
    order_btn = (
        By.XPATH,
        './/div[contains(@class, "Order_Content")]//button[text()="Заказать"]',
    )
    order_modal = By.XPATH, './/div[contains(@class, "Order_Modal")]'
    order_modal_yes_btn = By.XPATH, f'{order_modal[1]}//button[text()="Да"]'
    order_modal_success_text = (
        By.XPATH,
        f'{order_modal[1]}//div[text()="Заказ оформлен"]',
    )
    order_modal_show_status_btn = (
        By.XPATH,
        f'{order_modal[1]}//button[text()="Посмотреть статус"]',
    )

    @step('Ожидать появления элемента первой страницы формы заказа')
    def wait_for_first_name_visible(self) -> None:
        self.wait_until_element_visible(self.first_name_input)

    @step('Выбрать значение из списка для поля "Станция метро"')
    def set_metro_station(self, value: str) -> None:
        input = self.find_element(self.metro_station_input)
        input.click()
        input.parent.find_element(
            By.XPATH,
            (
                './/div[@class="select-search__select"]'
                f'//div[text()="{value}"]'
            )
        ).click()

    @step('Установить значение поля "Телефон"')
    def set_phone(self, value: str) -> None:
        self.set_text(self.phone_input, value)

    @step('Кликнуть по кнопке "Далее"')
    def click_next_btn(self) -> None:
        self.click(self.next_btn)

    @step('Заполнить перву страницу формы заказа')
    def fill_out_first_page(
        self,
        first_name: str,
        last_name: str,
        address: str,
        metro_station: str,
        phone: str,
    ) -> None:
        self.wait_for_first_name_visible()
        self.set_text(self.first_name_input, first_name)
        self.set_text(self.last_name_input, last_name)
        self.set_text(self.address_input, address)
        self.set_metro_station(metro_station)
        self.set_text(self.phone_input, phone)

    @step('Ожидать появления элемента второй страницы формы заказа')
    def wait_for_date_visible(self) -> None:
        self.wait_until_element_visible(self.date_input)

    @step('Установить значение поля даты доставки')
    def set_date(self, value: str) -> None:
        self.set_text(self.date_input, value, Keys.ENTER)

    @step('Установить значение поля срока аренды')
    def set_rental_period(self, value: str) -> None:
        element = self.find_element(self.rental_period_field)
        element.click()
        element.find_element(
            By.XPATH,
            f'../..//div[text()="{value}"]',
        ).click()

    @step('Установить чекбоксы цветов самоката')
    def set_colors(self, value: str) -> None:
        group = self.find_element(self.color_group)
        colors = value.split(',')
        for color in colors:
            group.parent.find_element(
                By.XPATH,
                f'.//label[text()="{color}"]',
            ).click()

    @step('Установить значение поля комментария')
    def set_comment(self, value: str) -> None:
        self.set_text(self.comment_input, value)

    @step('Заполнить поля второй страницы формы создания заказа')
    def fill_out_second_page(
        self,
        date: str,
        rental_period: str,
        colors: str,
        comment: str,
    ) -> None:
        self.wait_for_date_visible
        self.set_date(date)
        self.set_rental_period(rental_period)
        self.set_colors(colors)
        self.set_comment(comment)

    @step('Кликнуть по кнопке "Заказать"')
    def click_order_btn(self) -> None:
        self.click(self.order_btn)

    @step('Ожидать появления модального окна подтверждения заказа')
    def wait_for_order_modal_visible(self) -> None:
        self.wait_until_element_visible(self.order_modal)

    @step('Клинкуть по кнопке "Да" окна подтверждения заказа')
    def click_order_modal_yes_btn(self) -> None:
        self.click(self.order_modal_yes_btn)

    @step('Кликнуть по кнопке "Показать статус"')
    def click_order_modal_show_status_btn(self) -> None:
        self.click(self.order_modal_show_status_btn)
