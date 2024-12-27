import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)


    def click_element(self, locator):
        self.find(locator).click()


    @allure.step('скролит страницу вниз до конца')
    def scroll_down(self):
        windowScrollDown = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(windowScrollDown)


    @allure.step('Переходит на новую страницу')
    def switch_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)


    @allure.step('Ждет, пока прогрузится урл дзена')
    def wait_change_url_dzen(self):
        url_dzen = 'https://dzen.ru/?yredirect=true'
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url_dzen))