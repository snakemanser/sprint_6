from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_0 = [By.ID, 'accordion__heading-0']
    QUESTION_1 = [By.ID, 'accordion__heading-1']
    QUESTION_2 = [By.ID, 'accordion__heading-2']
    QUESTION_3 = [By.ID, 'accordion__heading-3']
    QUESTION_4 = [By.ID, 'accordion__heading-4']
    QUESTION_5 = [By.ID, 'accordion__heading-5']
    QUESTION_6 = [By.ID, 'accordion__heading-6']
    QUESTION_7 = [By.ID, 'accordion__heading-7']
    ANSWER_0 = [By.XPATH, "//div[@id='accordion__panel-0']/p"]
    ANSWER_1 = [By.XPATH, "//div[@id='accordion__panel-1']/p"]
    ANSWER_2 = [By.XPATH, "//div[@id='accordion__panel-2']/p"]
    ANSWER_3 = [By.XPATH, "//div[@id='accordion__panel-3']/p"]
    ANSWER_4 = [By.XPATH, "//div[@id='accordion__panel-4']/p"]
    ANSWER_5 = [By.XPATH, "//div[@id='accordion__panel-5']/p"]
    ANSWER_6 = [By.XPATH, "//div[@id='accordion__panel-6']/p"]
    ANSWER_7 = [By.XPATH, "//div[@id='accordion__panel-7']/p"]
    ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    BIG_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")

    LOGO_SCOOTER = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    LOGO_YANDEX = [By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"]
    IMG_SCOOTER = [By.XPATH, "//img[@src='/assets/blueprint.png']"]