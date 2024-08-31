import pytest


def test_homepage_menu(home_page):
    element = home_page.item("menu_home")
    assert element.is_visible(), f"Not found: {element._locator}"
    # element.highlight_and_make_screenshot("menu_home.png")


def test_homepage_sign_in(home_page):
    element = home_page.item("sign_in_button")
    assert element.is_visible(), f"Not found: {element._locator}"


def test_fail_path(home_page):
    with pytest.raises(AttributeError):
        element = home_page.item("sign_in_button2")
        element.is_visible()

def test_contact_header_visible(home_page):
    element = home_page.item("contacts_head")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_contact_section_visible(home_page):
    element = home_page.item("contact_section")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_homepage_sign_up(home_page):
    element = home_page.item("sign_up_button")
    assert element.is_visible(), f"Not found: {element._locator}"

