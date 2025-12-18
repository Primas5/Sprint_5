from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import StarterPageLocators
from locators import LoginMadalWindowLocators
from locators import MainPageLocators
from locators import Urls

class TestLogin:
    def test_succesful_login(self, webdriver_chrome):
        driver = webdriver_chrome
        driver.get(Urls.START_URL)
        #Нажать кнопку «Вход и регистрация».
        driver.find_element(*StarterPageLocators.LOGIN_AND_REGISTRTION_BUTTON).click()

        #Заполнить все поля формы авторизации и нажать кнопку «Войти».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginMadalWindowLocators.ENTER_EMAIL_FIELD))
        driver.find_element(*LoginMadalWindowLocators.ENTER_EMAIL_FIELD).send_keys('adoroshin@ya.ru')
        driver.find_element(*LoginMadalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*LoginMadalWindowLocators.LOGIN_BUTTON).click()

        #Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.EXIT_BUTTON))
        profile_name = driver.find_element(*MainPageLocators.PROFILE_NAME).text
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.PROFILE_BUTTON))
        profile_button = driver.find_element(*MainPageLocators.PROFILE_BUTTON).get_attribute('xmlns')
        assert "User." in profile_name
        assert Urls.DEFAULT_PROFILE_ICON_URL in profile_button