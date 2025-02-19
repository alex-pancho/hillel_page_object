from pages.base_page import BasePage


class Main(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        content_section='//section',
        subpages_left='//div[@style="transform: translateX(0px);"]',
        
        )