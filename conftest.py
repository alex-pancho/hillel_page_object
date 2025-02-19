import pytest
from get_browser import firefox, chrome

from pages.emailsignup import EmailSignup
from pages.login import Login
from pages.main_unreg import MainWOSign
from pages.main import Main


URL = "https://www.instagram.com"


@pytest.fixture(scope="module")
def driver():
    _driver = chrome(True)
    _driver.maximize_window()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture
def signup_page(driver):
    return EmailSignup(driver)


@pytest.fixture
def login_page(driver):
    return Login(driver)


@pytest.fixture
def main_wo_login(driver):
    return MainWOSign(driver)


@pytest.fixture
def main_page(driver):
    return Main(driver)
