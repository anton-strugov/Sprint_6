import pytest
from allure import title

from config import Config
from conftest import BaseTest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.header import Header


class TestOrder(BaseTest):
    @title('Проверка положительного сценария создания заказа')
    @pytest.mark.parametrize(
        (
            'btn_index,first_name,last_name,address,metro_station,phone,'
            'date,rental_period,colors,comment'
        ),
        [
            (
                0,
                'Игорь',
                'Потов',
                'Ленина 1',
                'Сокольники',
                '79999876543',
                '25.02.2026',
                'сутки',
                'чёрный жемчуг,серая безысходность',
                'Комментарий для курьера',
            ),
            (
                1,
                'Владимир',
                'Ленин',
                'Карла Маркса 7',
                'Ленинский проспект',
                '89876543210',
                '07.11.2026',
                'трое суток',
                'серая безысходность',
                'Пролетарии всех стран, соединятесь!',
            ),
        ]
    )
    def test_create_order(
        self,
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
    ):
        HomePage(self.driver).click_order(btn_index)
        order_page = OrderPage(self.driver)
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

        header = Header(self.driver)
        header.click_scooter_logo()
        assert header.is_url_equal(Config.BASE_URL)

        window_handles_count = len(self.driver.window_handles)
        header.click_yandex_logo()
        assert len(self.driver.window_handles) > window_handles_count
        self.driver.switch_to.window(self.driver.window_handles[-1])
        header.is_url_equal('https://dzen.ru/?yredirect=true')
