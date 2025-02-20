import pytest
import os
from get_browser import firefox, chrome

from pages.emailsignup import EmailSignup
from pages.login import Login
from pages.main_unreg import MainWOSign
from pages.main import Main


URL = "https://www.instagram.com"


@pytest.fixture(scope="module")
def driver():
    headlees = os.name == "nt"
    _driver = chrome(headlees) # by default run healess in linux
    _driver.maximize_window()
    yield _driver
    _driver.quit()


@pytest.fixture
def signup_page(driver):
    driver.get(f"{URL}/accounts/emailsignup/")
    return EmailSignup(driver)


@pytest.fixture
def login_page(driver):
    driver.get(f"{URL}/accounts/login/")
    return Login(driver)


@pytest.fixture
def main_wo_login(driver):
    driver.get(URL)
    return MainWOSign(driver)


@pytest.fixture
def main_page(driver):
    driver.get(URL)
    return Main(driver)
