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

def test_login_valid_user(home_page):
    username = "valid_user@example.com"
    password = "secure_password"

    username_element = home_page.item("username_by")
    password_element = home_page.item("password_by")
    signin_element = home_page.item("signin_by")

    username_element.send_keys = pytest.mock.Mock()
    password_element.send_keys = pytest.mock.Mock()
    signin_element.click = pytest.mock.Mock()

    home_page.login_valid_user(username, password)

    username_element.send_keys.assert_called_once_with(username)
    password_element.send_keys.assert_called_once_with(password)
    signin_element.click.assert_called_once()
