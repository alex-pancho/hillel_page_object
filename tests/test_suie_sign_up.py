import pytest


def test_is_exsist_login_with_facebook_button(signup_page):
    element = signup_page.item("login_with_facebook_button")
    assert element.is_visible(), f"Not found: {element._locator}"

def test_is_exsist_register_form(signup_page):
    mob_or_phone = signup_page.item("mobile_number_email_input")
    assert mob_or_phone.is_visible(), f"Not found: {mob_or_phone._locator}"

    password_input = signup_page.item("password_input")
    assert password_input.is_visible(), f"Not found: {password_input._locator}"

    full_name_input = signup_page.item("full_name_input")
    assert full_name_input.is_visible(), f"Not found: {full_name_input._locator}"
    
    username_input = signup_page.item("username_input")
    assert username_input.is_visible(), f"Not found: {username_input._locator}"