from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestRedirects:

    # тест проверяет, что при клике на лого "Самокат" происходит переход на главную, потому что есть картинка скутера
    def test_logo_scooter_redirect_main(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_logo_scooter()
        element = main_page.driver.find_element(*MainPageLocators.IMG_SCOOTER)
        assert element

    # тест проверяет, что после клика на лого яндекса урл содержит хост дзена
    def test_logo_yandex_redirect_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        # переключаемся на окно дзена
        main_page.switch_window()
        # ждем смены урла на дзеновский
        main_page.wait_change_url_dzen()
        current_url = driver.current_url
        assert 'https://dzen.ru' in current_url






