from pages.base_page import BasePage

class SignUp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        sign_up_button_initial='//button[@class="hero-descriptor_btn btn btn-primary"]',
        first_name='//input[@id="signupName"]',
        last_name='//input[@id="signupLastName"]',
        email='//input[@id="signupEmail"]',
        password='//input[@id="signupPassword"]',
        confirm_password='//input[@id="signupRepeatPassword"]',
        sign_up_button='//button[@class="btn btn-primary"]',
    )

    def open_sign_up_form(self):
        self.item("sign_up_button_initial").click()
    def fill_form(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str):
        self.item("first_name").send_keys(first_name)
        self.item("last_name").send_keys(last_name)
        self.item("email").send_keys(email)
        self.item("password").send_keys(password)
        self.item("confirm_password").send_keys(confirm_password)
        self.item("sign_up_button").click()

    def is_form_closed(self):
        try:
            return not self.item("sign_up_form").is_visible()
        except Exception:
            return True