from selenium import webdriver
import pytest

from config import Config


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()
