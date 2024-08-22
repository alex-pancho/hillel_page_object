import pytest


def test_add_new_car(garage_page):
    garage_page.add_new_car("BMW", 10)
    element = garage_page.item("new_car")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_log_out_of_the_page(garage_page):
    garage_page.log_out_of_the_page()
    assert garage_page.is_element_present("guest_btn"), "Log out failed"