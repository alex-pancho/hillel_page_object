from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        sign_up_button_in_header = "//header//ul/li[3]/a"
        )

    def open_sign_up_form(self):
        sign_button_element = self.item("sign_up_button_in_header")
        sign_button_element.click()
