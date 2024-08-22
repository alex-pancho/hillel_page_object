import pytest
from get_browser import firefox, chrome

from pages.home_page import HomePage
from pages.garage_page import GaragePage
from pages.fuel_expenses_page import FuelExpensesPage
from pages.instructions_page import InstructionsPage

URL = "https://guest:welcome2qauto@qauto.forstudy.space"

@pytest.fixture(scope="module")
def driver():
    _driver = chrome(True)
    _driver.maximize_window()
    _driver.get(URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def garage_page(driver):
    return GaragePage(driver)

@pytest.fixture
def fuel_expenses_page(driver):
    return FuelExpensesPage(driver)

@pytest.fixture
def instructions_page(driver):
    return InstructionsPage(driver)

