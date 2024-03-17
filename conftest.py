import pytest
from hillel_page_object.get_browser import firefox, chrome
from .pages.home_page import HomePage
from .pages.sign_up_page import SignUp
from .pages.cabinet_page import CabinetPage

URL = "https://magento.softwaretestingboard.com/"

@pytest.fixture(scope="function")
def driver():
    _driver = firefox()
    _driver.maximize_window()
    _driver.get(URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def sign_up_page(driver):
    return SignUp(driver)

@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver)