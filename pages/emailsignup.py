from pages.base_page import BasePage


class EmailSignup(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        login_with_facebook_button='//form[@class="_aah-"]//button[@type="button"]',

        mobile_number_email_input='//input[@aria-label="Mobile Number or Email"]',
        password_input='//input[@aria-label="Password"',
        full_name_input='//input[@aria-label="Full Name"]',
        username_input='//input[@aria-label="Username"]',

        signup_button='//button[.="Sign up"]',

        login_link='//a[@href="/accounts/login/?source=auth_switcher"]',
        
        gplay_app_button='//a[@aria-label="Get it on Google Play"]',
        msstore_button='//a[@aria-label="Get it from Microsoft"]',
        )

    def sign_up_new_user(self, number_or_mail, password, full_name, username):
        mobile_number_email_field = self.item("mobile_number_email_input")
        password_field = self.item("password_input")
        full_name_input_field = self.item("full_name_input")
        username_input_field = self.item("username_input")
        signup = self.item("signup_button")

        mobile_number_email_field.send_keys(number_or_mail)
        password_field.send_keys(password)
        full_name_input_field.send_keys(full_name)
        username_input_field.send_keys(username)
        signup.click()

