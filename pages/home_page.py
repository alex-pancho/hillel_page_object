from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        menu_home='//a[text()="Home"]',
        sign_in_button='//button[.="Sign In"]',
        contacts_head='//h2',
        sign_up_button='//button[.="Sign Up"]',
        username_by='//[@name="email"]',
        password_by='//*[@id="signinPassword"]',
        signin_by='//form//div[.="Login"]',
        contact_section='// * [ @ id = "contactsSection"] / div / div / div[2] / a[1]',
        guest_button='/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]'
        )

    def login_valid_user(self, username, password):
        username_by = self.item("username_by")
        password_by = self.item("password_by")
        signin_by = self.item("signin_by")

        username_by.send_keys(username)
        password_by.send_keys(password)
        signin_by.click()
