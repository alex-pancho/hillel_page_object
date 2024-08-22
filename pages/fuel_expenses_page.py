from pages.base_page import BasePage

class FuelExpensesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        guest_btn='//button[. = "Guest log in"]',
        fuel_expenses_page = '//a[@class="btn btn-white btn-sidebar sidebar_btn"][normalize-space()="Fuel expenses"]',
        add_expense = '//button[@class="btn btn-primary"]', # //button[contains(@class, 'btn') and contains(@class, 'btn-primary')]
        car_select = '//button[@id="carSelectDropdown"]',
        delete_expense = '//button[@class="btn btn-delete"]',
        edit_expense = '//button[@class="btn btn-edit"]',
        vehicle = '//*[@id="addExpenseCar"]', 
        report_date = '//*[@id="addExpenseDate"]',  
        mileage_1 ='//input[@id="mileage"]',
        number_of_liters ='//input[@id="addExpenseLiters"]',    # //*[@id="addExpenseLiters"]
        total_cost ='//input[@id="addExpenseTotalCost"]',
        cancel_button='//button[@class="btn btn-secondary" and text()="Cancel"]',
        save_button='//button[@class="btn btn-primary" and text()="Add"]',
        add_fuel_expense = '//li[@class="car-item"]'
    )

    def add_fuel_expens(self, vehicle: str, report_date: int, mileage_1: int, number_of_liters: int, total_cost: int):
        self.item("guest_btn").click()
        self.item(" fuel_expenses_page").click()
        self.item("add_expense").click()


        vehicle_select = self.item("vehicle")
        report_date_select = self.item("report_date")
        mileage_input_1 = self.item("mileage_1")
        number_of_liters_input = self.item("number_of_liters")
        total_cost_input = self.item("total_cost")
        save = self.item("save_button")

        vehicle_select.select(vehicle)
        report_date_select.select(report_date)
        mileage_input_1.send_keys(str(mileage_1))
        number_of_liters_input.send_keys(str(number_of_liters))
        total_cost_input.send_keys(str(total_cost))
        save.click()