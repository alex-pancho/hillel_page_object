from pages.base_page import BasePage

class InstructionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        guest_btn='//button[. = "Guest log in"]',
        instructions_tab='//a[@class="btn btn-white btn-sidebar sidebar_btn -active"]',
        brand_dropdown='//button[@id="brandSelectDropdown"]',
        model_dropdown='//button[@id="modelSelectDropdown"]',
        search_button='//button[@class="instructions-search-controls_search btn btn-primary"]',
        search_results = '//a[@class="instruction-link" and @href="https://qauto2.forstudy.space/public/instructions/bmw/3/Engine oil and filter on BMW 3.pdf"]',
        download_link_1='//li[1]//a[1]//a[1]',
        download_link_2='//li[2]//a[1]//a[1]',
        download_link_3='//li[3]//a[1]//a[1]',
        download_link_4='//li[4]//a[1]//a[1]'
    )

    def select_car_and_search(self, brand: str, model: str):
        self.item("guest_btn").click()
        self.item("instructions_tab").click()
        self.item("brand_dropdown").select(brand)
        self.item("model_dropdown").select(model)
        self.item("search_button").click()

    def download_instruction(self, link_number: int):
        download_link = f'download_link_{link_number}'
        self.item(download_link).click()