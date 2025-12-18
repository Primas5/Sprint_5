import random

from selenium.webdriver.common.by import By

class Urls:
    START_URL = "https://qa-desk.stand.praktikum-services.ru/"
    DEFAULT_PROFILE_ICON_URL = "http://www.w3.org/2000/svg"

class StarterPageLocators: # Стартовая страница
    LOGIN_AND_REGISTRTION_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    POST_ADVERTISEMENT_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")

class LoginMadalWindowLocators: # Модальное окно "Войти"
    MESSAGE_AFTER_POST_ADVERTISEMENT_BUTTON = (By.XPATH, ".//div/form/div/h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    ENTER_EMAIL_FIELD = (By.NAME, "email")
    ENTER_PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    
class RegisterNodalWindowLocators: # Модальное окно "Зарегистрироваться" при клике на "Нет акккаунта" в модальном окне "Войти"
    ENTER_EMAIL_FIELD = (By.NAME, "email")
    ENTER_PASSWORD_FIELD = (By.NAME, "password")
    REPEAT_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ALREADY_EXIST_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Уже есть аккаунт']")
    RED_EMAIL_ERROR_MESSAGE = (By.XPATH, ".//div[1]/span[@class='input_span__yWPqB']")
    FIRST_RED_ERROR_BORDER = (By.XPATH, ".//div[1]/div/div[@class='input_inputError__fLUP9']")
    SECOND_RED_ERROR_BORDER = (By.XPATH, ".//div[2]/div/div[@class='input_inputError__fLUP9']")
    THIRD_RED_ERROR_BORDER = (By.XPATH, ".//div[3]/div/div[@class='input_inputError__fLUP9']")

class MainPageLocators: #Главная страница после регистрации или входа
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    PROFILE_BUTTON = (By.XPATH, ".//div[@class='flexRow']/button/*")

class AdvertisementCreatePage: #Страница для создания объявления
    TITLE_FIELD = (By.XPATH, ".//input[@placeholder='Название']")
    DESCRIPTION_PRODUCT_FIELD = (By.XPATH, ".//textarea[@placeholder='Описание товара']")
    PRICE_FIELD = (By.XPATH, ".//input[@placeholder='Стоимость']")
    CATEGOTY_DROPDOWN = (By.XPATH, ".//div[2]/div/div[1]/button[1][@type='button']")
    GARDENING_CATEGOTY_TEXT_OF_DROPDOWN = (By.XPATH, ".//div[2]/div/div[2]/button[3][@type='button']")
    CITY_DROPDOWN = (By.XPATH, ".//div[3]/div[1]/button[1][@type='button']")
    KAZAN_CITY_TEXT_OF_DROPDOWN = (By.XPATH, ".//div[3]/div[2]/button[6][@type='button']")
    ITEM_CONDITION_REGULAR_RADIOBUTTON = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']")
    PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    PROFILE_BUTTON = (By.XPATH, ".//div[@class='flexRow']/button")
    MY_ADS_MESSAGE = (By.XPATH, ".//h1[text()='Мои объявления']")
    CREATED_CARD_NAME_MESSAGE = (By.XPATH, ".//div/div/div[@class='card']/div[@class='description']/div[@class='about']/h2")
    CREATED_CARD_CITY_MESSAGE = (By.XPATH, ".//div/div/div[@class='card']/div[@class='description']/div[@class='about']/h3") 
    CREATED_CARD_PRICE_MESSAGE = (By.XPATH, ".//div/div/div[@class='card']/div[@class='description']/div[@class='price']/h2")