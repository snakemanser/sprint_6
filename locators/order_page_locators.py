from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_SOKOLNIKI_BUTTON = [By.XPATH, "//button[@value='4']"]  # кнопка выбора метро в выпадающем списке
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[contains(text(),'Далее')]"]

    DELIVERY_DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    DATE_30122024 = [By.XPATH, "//div[@aria-label='Choose понедельник, 30-е декабря 2024 г.']"]
    RENTAL_DATE_FIELD = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]
    RENTAL_DAY = [By.XPATH, "//div[contains(text(),'сутки')]"]  # "сутки" в выпадающем списке "Срок аренды"
    ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    YES_BUTTON = [By.XPATH, "//button[contains(text(),'Да')]"]
    ORDER_COMPLETED_TEXT = [By.XPATH, "//div[contains(text(),'Заказ оформлен')]"]

