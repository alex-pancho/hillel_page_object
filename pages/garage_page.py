from pages.base_page import BasePage


class GaragePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        add_car='//button[@class="btn btn-primary"]',
        brand='//*[@id="addCarBrand"]',
        model='',  # TODO: add the xpath here
        mileage='//*[@id="addCarMileage"]',
        add='//button[. = "Add"]',
        new_car='//li[@class="car-item"]',
        guest_btn='//button[. = "Guest log in"]',
        edit_car_icon="//span[@class='icon icon-edit']",
        remove_car_button="//button[@class='btn btn-outline-danger']",
        approve_remove_car_button="//button[@class='btn btn-danger']"
    )

    def add_new_car(self, brand: str,  mileage: int, model: str = "",):
        self.item("guest_btn").click()
        self.item("add_car").click()

        brand_select = self.item("brand")
        # import sys, pdb
        # pdb.Pdb(stdout=sys.stdout).set_trace()
        # model_select = self.item("model")
        mileage_input = self.item("mileage")
        add_button = self.item("add")

        brand_select.select(brand)
        mileage_input.send_keys(str(mileage))
        add_button.click()

    def delete_car(self):
        self.item("edit_car_icon").click()
        self.item("remove_car_button").click()
        self.item("approve_remove_car_button").click()
