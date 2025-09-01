from selenium.webdriver.support import expected_conditions as exp_conds
from selenium.webdriver.support.wait import WebDriverWait as wd_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from allure import step

from config import Config
from pages.base_page import BasePage


class HomePage(BasePage):
    order_btns = By.XPATH, './/button[text()="Заказать"]'
    questions = By.CLASS_NAME, 'accordion__item'
    question_btn = By.CLASS_NAME, 'accordion__button'
    answer = By.XPATH, './/div[@class="accordion__panel"]/p'

    @step('Перейти на домашнюю страницу')
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    @step('Кликнуть по кнопке "Заказать"')
    def click_order(self, index: int) -> None:
        btn = self.find_elements(self.order_btns)[index]
        self.driver.execute_script('arguments[0].scrollIntoView(true);', btn)
        btn.click()

    @step('Получить элемент списка вопросов по индексу')
    def get_question_item(self, index: int) -> WebElement:
        return self.find_elements(self.questions)[index]

    @step('Ожидать появления элемента списка вопросов по индексу')
    def wait_for_question_clickable(self, index: int) -> None:
        wd_wait(self.driver, Config.TIMEOUT).until(
            exp_conds.visibility_of(
                self.get_question_item(index).find_element(*self.question_btn),
            ),
        )

    @step('Кликнуть по строке вопроса')
    def click_question(self, index: int) -> None:
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);',
            self.get_question_item(index).find_element(*self.question_btn)
        )
        self.wait_for_question_clickable(index)
        self.get_question_item(index).find_element(*self.question_btn).click()

    @step('Получить текст вопроса по индексу')
    def get_question_text(self, index: int) -> str:
        return self.get_question_item(index).find_element(
            *self.question_btn,
        ).text

    @step('Ожидать появления ответа по индексу')
    def wait_for_answer_visible(self, index: int) -> None:
        wd_wait(self.driver, Config.TIMEOUT).until(
            exp_conds.visibility_of(
                self.get_question_item(index).find_element(*self.answer),
            ),
        )

    @step('Получить текст ответа по индексу')
    def get_answer_text(self, index: int) -> str:
        return self.get_question_item(index).find_element(*self.answer).text
