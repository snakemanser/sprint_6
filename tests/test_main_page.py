import pytest
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    # тест проверяет текст ответов на "Вопросы о важном"
    @pytest.mark.parametrize("question, answer, text", [
        (MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_check_answer_text(self, driver, question, answer, text):
        answer_text = text
        main_page = MainPage(driver)
        assert answer_text == main_page.return_answer_text(question, answer)





