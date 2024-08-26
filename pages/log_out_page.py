from pages.base_page import BasePage

class LogOut(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        guest_btn='//button[@class="header-link -guest"]',
        logout_button='//a[contains(@class, "btn-sidebar") and contains(@class, "text-danger")]',
    )

    def log_out(self):
        self.item("guest_btn").click()
        self.item("logout_button").click()