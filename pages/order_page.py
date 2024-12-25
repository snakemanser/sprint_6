from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_metro_sokolniki(self):
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderPageLocators.METRO_SOKOLNIKI_BUTTON).click()

    def set_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def set_delivery_date_30122024(self):
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.DATE_30122024).click()

    def set_rental_date_one_day(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_DATE_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_DAY).click()

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def return_order_completed_text(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_COMPLETED_TEXT).text














