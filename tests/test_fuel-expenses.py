import pytest

def test_add_an_expense(fuel_expenses_page):
    fuel_expenses_page.add_fuel_expens("BMW", "19.08.2024", 11, 4, 10000)
    element = fuel_expenses_page.item("add_fuel_expense")
    assert element.is_visible(), f"Not found: {element._locator}"