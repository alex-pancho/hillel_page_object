import pytest
from conftest import driver, garage_page


def test_add_new_car(garage_page):
    garage_page.add_new_car("BMW", 10)
    element = garage_page.item("new_car")
    assert element.is_visible(), f"Not found: {element._locator}"


def test_delete_new_car(garage_page):
    garage_page.delete_car()
    element = garage_page.item("new_car")
    assert not element.is_visible()


if __name__ == '__main__':
    pytest.main()
