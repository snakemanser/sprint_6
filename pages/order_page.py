from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def set_name(self, name):
        self.find(OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.find(OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.find(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_metro_sokolniki(self):
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(OrderPageLocators.METRO_SOKOLNIKI_BUTTON)

    def set_phone(self, phone):
        self.find(OrderPageLocators.PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def set_delivery_date_30122024(self):
        self.click_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.click_element(OrderPageLocators.DATE_30122024)

    def set_rental_date_one_day(self):
        self.click_element(OrderPageLocators.RENTAL_DATE_FIELD)
        self.click_element(OrderPageLocators.RENTAL_DAY)

    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def click_yes_button(self):
        self.click_element(OrderPageLocators.YES_BUTTON)

    def return_order_completed_text(self):
        return self.find(OrderPageLocators.ORDER_COMPLETED_TEXT).text













