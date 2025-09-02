import pytest
from allure import title
from selenium.webdriver.remote.webdriver import WebDriver

from config import Config
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.header import Header
from test_data.order_page_data import orders


class TestOrder:
    @title('Проверка положительного сценария создания заказа')
    @pytest.mark.parametrize(
        (
            'btn_index,first_name,last_name,address,metro_station,phone,'
            'date,rental_period,colors,comment'
        ),
        orders,
    )
    def test_create_order(
        self,
        driver: WebDriver,
        btn_index: int,
        first_name: str,
        last_name: str,
        address: str,
        metro_station: str,
        phone: str,
        date: str,
        rental_period: str,
        colors: str,
        comment: str,
    ) -> None:
        HomePage(driver).click_order(btn_index)
        order_page = OrderPage(driver)
        order_page.fill_out_first_page(
            first_name,
            last_name,
            address,
            metro_station,
            phone,
        )
        order_page.click_next_btn()
        order_page.fill_out_second_page(
            date,
            rental_period,
            colors,
            comment,
        )
        order_page.click_order_btn()
        order_page.wait_for_order_modal_visible()
        order_page.click_order_modal_yes_btn()
        assert order_page.is_element_visible(
            order_page.order_modal_success_text,
        )
        order_page.click_order_modal_show_status_btn()

        header = Header(driver)
        header.click_scooter_logo()
        assert header.is_url_equal(Config.BASE_URL)

        tabs_count = header.get_tabs_count()
        header.click_yandex_logo()
        assert header.get_tabs_count() > tabs_count
        header.switch_to_new_tab()
        header.is_url_equal('https://dzen.ru/?yredirect=true')
