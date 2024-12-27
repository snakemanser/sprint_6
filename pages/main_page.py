import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Возвращает текст ответа на вопрос из "Вопросы о важном"')
    def return_answer_text(self, question_locator, answer_locator):
        self.scroll_down()
        self.click_element(question_locator)
        return self.find(answer_locator).text


    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)


    def click_big_order_button(self):
        self.scroll_down()
        self.click_element(MainPageLocators.BIG_ORDER_BUTTON)


    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)


    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)










