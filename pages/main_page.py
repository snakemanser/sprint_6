import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('скролит страницу вниз до конца')
    def scroll_down(self):
        windowScrollDown = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(windowScrollDown)

    def click_question(self, locator):
        self.scroll_down()
        self.driver.find_element(*locator).click()

    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    def click_big_order_button(self):
        self.scroll_down()
        self.driver.find_element(*MainPageLocators.BIG_ORDER_BUTTON).click()

    @allure.step('Возвращает текст ответа на вопрос из "Вопросы о важном"')
    def return_answer_text(self, question_locator, answer_locator):
        self.scroll_down()
        self.click_question(question_locator)
        return self.driver.find_element(*answer_locator).text

    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    @allure.step('Переходит на новую страницу')
    def switch_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    @allure.step('Ждет, пока прогрузится урл дзена')
    def wait_change_url_dzen(self):
        url_dzen = 'https://dzen.ru/?yredirect=true'
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url_dzen))









