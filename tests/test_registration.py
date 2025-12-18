from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import StarterPageLocators
from locators import LoginMadalWindowLocators
from locators import RegisterNodalWindowLocators
from locators import MainPageLocators
from locators import Urls

import random
import string

def generate_random_email():
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    domains = ["ya.ru","gmail.com", "yahoo.com", "outlook.com", "example.ru", "test.net"]
    domain = random.choice(domains)
    
    email = f"{username}@{domain}"
    return email

def generate_bad_email():
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return username

class TestRegistration:
    def test_succesful_register(self, webdriver_chrome):
        #Нажать кнопку «Вход и регистрация».
        driver = webdriver_chrome
        driver.get(Urls.START_URL)
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()

        #Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*LoginMadalWindowLocators.NO_ACCOUNT_BUTTON).click()

        #Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.ENTER_EMAIL_FIELD))
        driver.find_element(*RegisterNodalWindowLocators.ENTER_EMAIL_FIELD).send_keys(generate_random_email())
        driver.find_element(*RegisterNodalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.REPEAT_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.CREATE_ACCOUT_BUTTON).click()

        #Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.EXIT_BUTTON))
        profile_name = driver.find_element(*MainPageLocators.PROFILE_NAME).text
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_BUTTON))
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON).get_attribute('xmlns')
        assert "User." in profile_name
        assert Urls.DEFAULT_PROFILE_ICON_URL in profile_button
        
    def test_wrong_mail_format_register(self, webdriver_chrome):
        driver = webdriver_chrome
        driver.get(Urls.START_URL)
        #Нажать кнопку «Вход и регистрация».
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()

        #Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*LoginMadalWindowLocators.NO_ACCOUNT_BUTTON).click()

        #Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.ENTER_EMAIL_FIELD))
        bad_email = generate_bad_email()
        driver.find_element(*RegisterNodalWindowLocators.ENTER_EMAIL_FIELD).send_keys(bad_email)
        driver.find_element(*RegisterNodalWindowLocators.CREATE_ACCOUT_BUTTON).click()

        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.RED_EMAIL_ERROR_MESSAGE))
        error_name = driver.find_element(*RegisterNodalWindowLocators.RED_EMAIL_ERROR_MESSAGE).text
        error_border1 = driver.find_element(*RegisterNodalWindowLocators.FIRST_RED_ERROR_BORDER).value_of_css_property('border-color')
        error_border2 = driver.find_element(*RegisterNodalWindowLocators.SECOND_RED_ERROR_BORDER).value_of_css_property('border-color')
        error_border3 = driver.find_element(*RegisterNodalWindowLocators.THIRD_RED_ERROR_BORDER).value_of_css_property('border-color')
        assert "Ошибка" in error_name
        assert "rgb(255, 105, 114)" == error_border1
        assert "rgb(255, 105, 114)" == error_border2
        assert "rgb(255, 105, 114)" == error_border3

    def test_email_already_register(self, webdriver_chrome):
        driver = webdriver_chrome
        driver.get(Urls.START_URL)
        #Нажать кнопку «Вход и регистрация».
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()

        #Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*LoginMadalWindowLocators.NO_ACCOUNT_BUTTON).click()

        # Дождаться закрытия модального окна входа
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(LoginMadalWindowLocators.NO_ACCOUNT_BUTTON))

        #Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.ENTER_EMAIL_FIELD))
        driver.find_element(*RegisterNodalWindowLocators.ENTER_EMAIL_FIELD).send_keys('adoroshin@ya.ru')
        driver.find_element(*RegisterNodalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.REPEAT_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.CREATE_ACCOUT_BUTTON).click()

        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.RED_EMAIL_ERROR_MESSAGE))
        error_name = driver.find_element(*RegisterNodalWindowLocators.RED_EMAIL_ERROR_MESSAGE).text
        error_border1 = driver.find_element(*RegisterNodalWindowLocators.FIRST_RED_ERROR_BORDER).value_of_css_property('border-color')
        error_border2 = driver.find_element(*RegisterNodalWindowLocators.SECOND_RED_ERROR_BORDER).value_of_css_property('border-color')
        error_border3 = driver.find_element(*RegisterNodalWindowLocators.THIRD_RED_ERROR_BORDER).value_of_css_property('border-color')
        assert "Ошибка" in error_name
        assert "rgb(255, 105, 114)" == error_border1
        assert "rgb(255, 105, 114)" == error_border2
        assert "rgb(255, 105, 114)" == error_border3