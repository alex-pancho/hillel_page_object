import pytest
import time
from get_browser import chrome
from tori_pageobject.pages.login_page import LoginPage as LP


URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.fixture(scope="function")
def driver():
    _driver = chrome()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture()
def login_page(driver):
    time.sleep(3)
    return LP(driver)
