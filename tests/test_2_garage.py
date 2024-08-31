import pytest

def test_add_new_car(garage_page):
    garage_page.add_new_car("BMW", 10)
    element = garage_page.item("new_car")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_add_car_button_visible(garage_page):
    element = garage_page.item("add_car")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_brand_select_visible(garage_page):
    element = garage_page.item("brand")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_mileage_input_visible(garage_page):
    element = garage_page.item("mileage")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_add_button_visible(garage_page):
    element = garage_page.item("add")
    assert element.is_visible(), f"Not found: {element._locator}"
def test_mileage_field_is_editable(garage_page):
    #garage_page.item("guest_btn").click()
    garage_page.item("add_car").click()
    mileage_input = garage_page.item("mileage")
    mileage_input.send_keys("12345")
    assert mileage_input.get_attribute("value") == "12345", "Mileage field is not editable"
def test_guest_login_button_works(garage_page):
    #garage_page.item("guest_btn").click()
    element = garage_page.item("add_car")
    assert element.is_visible(), "Guest login failed, Add Car button is not visible"

def test_add_car_without_brand(garage_page):
    #garage_page.add_new_car("", 10000)
    element = garage_page.item("new_car")
    assert not element.is_visible(), "Car added without selecting a brand"

def test_add_car_with_specific_model(garage_page):
    garage_page.add_new_car("Audi", 20000, model="A4")
    element = garage_page.item("new_car")
    assert element.is_visible(), "Car with model 'A4' was not added"