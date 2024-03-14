from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        username_field_xpath="//input[@placeholder='Username']",
        password_field_xpath="//input[@placeholder='Password']",
        login_button_xpath="//button[@type='submit']",
        error_message_xpath_1="(//div[@class='oxd-input-group oxd-input-field-bottom-space']//span)[1]",
        error_message_xpath_2="(//div[@class='oxd-input-group oxd-input-field-bottom-space']//span)[2]",
        reset_password_button_xpath="//div[@class='orangehrm-login-forgot']//p[1]",
    )
