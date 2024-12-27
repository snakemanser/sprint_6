import allure
import pytest
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.description(
        'тест проверяет сценарий оформления заказа для обеих кнопок "Заказать", от нажатия на кнопку "Заказать" до окна об успешном оформлении заказа')
    @pytest.mark.parametrize("name, surname, address, phone", [
        ('Пиджак', 'Течкович', 'На мидочек', '88005553535'),
        ('Падж', 'Хукович', 'Тоже на мидочек', '88000000000')
    ])
    def test_order_a_scooter_with_both_order_buttons(self, driver, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        if name == 'Пиджак':
            main_page.click_order_button()
        elif name == 'Падж':
            main_page.click_big_order_button()
        else:
            raise ValueError(f'Такого пуджа не знаю: {name}')
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro_sokolniki()
        order_page.set_phone(phone)
        order_page.click_next_button()
        order_page.set_delivery_date_30122024()
        order_page.set_rental_date_one_day()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert 'Заказ оформлен' in order_page.return_order_completed_text()


