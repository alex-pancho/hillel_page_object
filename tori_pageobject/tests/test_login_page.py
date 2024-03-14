"""
POSITIVE AND NEGATIVE TEST FOR HOME PAGE https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
"""
import os
from dotenv import load_dotenv
from tori_pageobject.conftest import driver, login_page

load_dotenv()

user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')


def test_login_button(driver, login_page):
    """Test that the login button is visible and functionally"""
    element = login_page.item('login_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    e_username = login_page.item('username_field_xpath')
    e_password = login_page.item('password_field_xpath')
    e_username.send_keys(user_name)
    e_password.send_keys(password)

    element.click()
    assert 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index' == driver.current_url, \
        f"It seems homepage button has incorrect link! Current url: {driver.current_url}"


def test_validation(login_page):
    """Test that both field are required"""
    element = login_page.item('login_button_xpath')
    element.click()

    error_mess_1 = login_page.item('error_message_xpath_1')
    error_mess_2 = login_page.item('error_message_xpath_2')

    assert 'Required' in error_mess_1.get_text()
    assert 'Required' in error_mess_2.get_text()


def test_reset_password_button(driver, login_page):
    """Test that the button 'Forgot password?' is visible and functionally"""
    element = login_page.item('reset_password_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    assert 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode' == driver.current_url, \
        f"It seems homepage button has incorrect link! Current url: {driver.current_url}"



