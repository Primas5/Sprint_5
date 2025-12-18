from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import StarterPageLocators
from locators import LoginMadalWindowLocators
from locators import RegisterNodalWindowLocators
from locators import AdvertisementCreatePage
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

class TestCreateAD:
    def test_create_advertisement_without_login(self, webdriver_chrome):
        driver = webdriver_chrome
        driver.get(Urls.START_URL)
        #Нажать кнопку «Разместить объявление».
        driver.find_element(*StarterPageLocators.POST_ADVERTISEMENT_BUTTON).click()

        #Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.MESSAGE_AFTER_POST_ADVERTISEMENT_BUTTON))
        assert 'Чтобы разместить объявление, авторизуйтесь' in driver.find_element(*LoginMadalWindowLocators.MESSAGE_AFTER_POST_ADVERTISEMENT_BUTTON).text

    def test_succesful_create_advertisement(self, webdriver_chrome):
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
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginMadalWindowLocators.LOGIN_BUTTON))
        driver.find_element(*LoginMadalWindowLocators.LOGIN_BUTTON).click()

        # Дождаться закрытия модального окна входа
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(LoginMadalWindowLocators.LOGIN_BUTTON))

        #Нажать кнопку «Разместить объявление».
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StarterPageLocators.POST_ADVERTISEMENT_BUTTON))
        driver.find_element(*StarterPageLocators.POST_ADVERTISEMENT_BUTTON).click()

        #Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.TITLE_FIELD))
        driver.find_element(*AdvertisementCreatePage.TITLE_FIELD).send_keys('Замок')
        driver.find_element(*AdvertisementCreatePage.DESCRIPTION_PRODUCT_FIELD).send_keys('Замок для хорошего времяпровождения')
        driver.find_element(*AdvertisementCreatePage.PRICE_FIELD).send_keys('999999999')

        #Выбрать из Dropdown «Категорию» и «Город».
        driver.find_element(*AdvertisementCreatePage.CATEGOTY_DROPDOWN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.GARDENING_CATEGOTY_TEXT_OF_DROPDOWN))
        driver.find_element(*AdvertisementCreatePage.GARDENING_CATEGOTY_TEXT_OF_DROPDOWN).click()
        driver.find_element(*AdvertisementCreatePage.CITY_DROPDOWN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.KAZAN_CITY_TEXT_OF_DROPDOWN))
        driver.find_element(*AdvertisementCreatePage.KAZAN_CITY_TEXT_OF_DROPDOWN).click()

        #Выбрать RabioButton «Состояние товара».
        driver.find_element(*AdvertisementCreatePage.ITEM_CONDITION_REGULAR_RADIOBUTTON).click()

        #Нажать кнопку «Опубликовать».
        driver.find_element(*AdvertisementCreatePage.PUBLISH_BUTTON).click()

        # Дождаться закрытия окна входа
        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located(AdvertisementCreatePage.PUBLISH_BUTTON))

        #Перейти в профиль пользователя.
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AdvertisementCreatePage.PROFILE_BUTTON))
        driver.find_element(*AdvertisementCreatePage.PROFILE_BUTTON).click()
        
        #Проверить: в блоке «Мои объявления» отображается созданное объявление.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.MY_ADS_MESSAGE))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.CREATED_CARD_NAME_MESSAGE))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.CREATED_CARD_CITY_MESSAGE))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AdvertisementCreatePage.CREATED_CARD_PRICE_MESSAGE))

        assert 'Замок' in driver.find_element(*AdvertisementCreatePage.CREATED_CARD_NAME_MESSAGE).text
        assert  'Казань' in driver.find_element(*AdvertisementCreatePage.CREATED_CARD_CITY_MESSAGE).text
        assert  '999 999 999' in driver.find_element(*AdvertisementCreatePage.CREATED_CARD_PRICE_MESSAGE).text