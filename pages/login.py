from pages.base_page import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        mobile_number_email_input='//input[@aria-label="Phone number, username, or email"]',
        password_input='//input[@aria-label="Password"',
        login_button='//button/div[.="Log in"]',
        
        login_with_facebook_link='//button//div[.="Log in with Facebook"]',
        forgot_password_link='//a[@href="/accounts/password/reset/"]',

        signup_link='//a[@href="/accounts/emailsignup/"]',

        gplay_app_button='//a[@aria-label="Get it on Google Play"]',
        msstore_button='//a[@aria-label="Get it from Microsoft"]',
        )

    def exsist_user_login(self, number_or_mail, password):
        mobile_number_email_field = self.item("mobile_number_email_input")
        password_field = self.item("password_input")
        login = self.item("login_button")

        mobile_number_email_field.send_keys(number_or_mail)
        password_field.send_keys(password)
        login.click()