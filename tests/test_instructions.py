import pytest
from pages.instructions_page import InstructionsPage

@pytest.fixture
def instructions_page(driver):
    return InstructionsPage(driver)

def test_select_car_and_search(instructions_page):
    brand = "BMW"
    model = "3"

    instructions_page.select_car_and_search(brand, model)
    assert instructions_page.is_visible("search_results"), "Search results are not displayed"

@pytest.mark.parametrize("link_number", [1, 2, 3, 4])
def test_download_instruction(instructions_page, link_number):
    instructions_page.download_instruction(link_number)
    assert instructions_page.is_visible(f"download_link_{link_number}"), f"Download link {link_number} is not visible"