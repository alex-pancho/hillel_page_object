from .base_page import BasePage


class CabinetPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        my_account_title = "//span[@class='base' and text()='My Account']"
        )

    def get_page_title(self):
        title_element = self.item("my_account_title").get_text()
        return title_element