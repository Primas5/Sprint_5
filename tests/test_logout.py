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

class TestLogout:
    def test_succesful_logout(self, webdriver_chrome):
        driver = webdriver_chrome
        driver.get(Urls.START_URL)

        #Создание аккаута и выход из него перед тестом
        #Нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON))
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()

        #Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginMadalWindowLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*LoginMadalWindowLocators.NO_ACCOUNT_BUTTON).click()

        #Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        generated_email = generate_random_email()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterNodalWindowLocators.ENTER_EMAIL_FIELD))
        driver.find_element(*RegisterNodalWindowLocators.ENTER_EMAIL_FIELD).send_keys(generated_email)
        driver.find_element(*RegisterNodalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.REPEAT_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegisterNodalWindowLocators.CREATE_ACCOUT_BUTTON).click()

        #Нажать кнопку «Выйти».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()

        # Дождаться выхода из профиля
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(MainPageLocators.EXIT_BUTTON))

        #Основной тест
        #Авторизоваться под заранее созданным пользователем.
        #Нажать кнопку «Вход и регистрация».
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()
        #Заполнить все поля формы авторизации и нажать кнопку «Войти».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.ENTER_EMAIL_FIELD))
        driver.find_element(*LoginMadalWindowLocators.ENTER_EMAIL_FIELD).send_keys(generated_email)
        driver.find_element(*LoginMadalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*LoginMadalWindowLocators.LOGIN_BUTTON).click()

        #Нажать кнопку «Выйти».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()

        #Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», 
        #там теперь отображается кнопка «Вход и регистрация».
        try:
            WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.EXIT_BUTTON))
            profile_name = driver.find_element(*MainPageLocators.PROFILE_NAME).text
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_BUTTON))
            profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON).get_attribute('xmlns')
            assert "User." not in profile_name
            assert Urls.DEFAULT_PROFILE_ICON_URL not in profile_button
        except:
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON))
            assert "Вход и регистрация" in driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).text