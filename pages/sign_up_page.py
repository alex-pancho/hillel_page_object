from .base_page import BasePage


class SignUp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        first_name_field="//input[@id='firstname']",
        last_name_field="//input[@id='lastname']",
        email_field="//input[@id='email_address']",
        password_field="//input[@id='password']",
        confirm_password_field="//input[@id='password-confirmation']",
        create_account_button="//button[@title='Create an Account']",
        invalid_email_error="//div[@id='email_address-error']",
        first_name_error="//div[@id='firstname-error']",
        last_name_error="//div[@id='lastname-error']",
        email_field_error="//div[@id='email_address-error']",
        password_field_error="//div[@id='password-error']",
        confirm_password_field_error="//div[@id='password-confirmation-error']"
    )

    def sign_up(self, firstname, lastname, email, password, repeated_password):
        first_name_field_element = self.item("first_name_field")
        first_name_field_element.send_keys(firstname)

        last_name_field_element = self.item("last_name_field")
        last_name_field_element.send_keys(lastname)

        email_field_field_element = self.item("email_field")
        email_field_field_element.send_keys(email)

        password_field_element = self.item("password_field")
        password_field_element.send_keys(password)

        confirm_password_field_element = self.item("confirm_password_field")
        confirm_password_field_element.send_keys(repeated_password)

        create_account_button_element = self.item("create_account_button")
        create_account_button_element.scroll_to_element()
        create_account_button_element.click()

    def get_invalid_email_error_text(self):
        invalid_error_message = self.item("invalid_email_error").get_text()
        return invalid_error_message

    def get_required_field_error(self):
        first_name_error = self.item("first_name_error").get_text()
        last_name_error = self.item("last_name_error").get_text()
        email_error = self.item("email_field_error").get_text()
        password_error = self.item("password_field_error").get_text()
        confirm_password_error = self.item("confirm_password_field_error").get_text()
        return {
            "first_name_error": first_name_error,
            "last_name_error": last_name_error,
            "email_error": email_error,
            "password_error": password_error,
            "confirm_password_error": confirm_password_error
        }


