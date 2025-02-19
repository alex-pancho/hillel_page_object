from pages.login import Login


class MainWOSign(Login):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        iphone_image='//article//img'
        )

