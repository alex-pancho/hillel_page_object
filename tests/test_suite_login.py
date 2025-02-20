import pytest


def test_is_exsist_login_with_facebook_button(signup_page):
    element = signup_page.item("login_with_facebook_button")
    assert element.is_visible(), f"Not found: {element._locator}"
