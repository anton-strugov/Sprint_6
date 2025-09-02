import pytest
from allure import title
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from test_data.home_page_data import faq


class TestHomePage:
    @title('Проверка раскртия вопросов и соттветствия ответов вопросам')
    @pytest.mark.parametrize('index,question,answer', faq)
    def test_question(
        self,
        driver: WebDriver,
        index: int,
        question: str,
        answer: str,
    ) -> None:
        home_page = HomePage(driver)
        home_page.click_question(index)
        home_page.wait_for_answer_visible(index)
        assert home_page.get_question_text(index) == question
        assert home_page.get_answer_text(index) == answer
