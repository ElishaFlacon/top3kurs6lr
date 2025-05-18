import time

from selenium.webdriver.common.by import By
from selenium import webdriver

import pytest


AWAIT_TIME = 2
BETWEEN_TIME = 1

LOGIN_ID = 'login'
PASSWORD_ID = 'password'

LOGIN_ERROR_XPATH = '/html/body/esia-root/div/esia-login/div/div[1]/form/div[1]/div'
PASSWORD_ERROR_XPATH = '/html/body/esia-root/div/esia-login/div/div[1]/form/div[3]/div'

LOGIN_BTN_XPATH = '/html/body/esia-root/div/esia-login/div/div[1]/form/div[4]/button'
FORGOT_PASSWORD_XPATH = '/html/body/esia-root/div/esia-login/div/div[1]/form/div[3]/button'
REGISTRATION_LINK_XPATH = '/html/body/esia-root/div/esia-login/div/div[2]/button'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_driver_start(driver):
    driver.get('https://esia.gosuslugi.ru/login')


def test_successful_login(driver):
    driver.find_element(By.ID, LOGIN_ID).send_keys("email@mail.ru")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
        assert False, "Система показывает ошибку при корректных данных"
    except:
        pass


def test_invalid_credentials(driver):
    driver.find_element(By.ID, LOGIN_ID).send_keys("wrong_email@mail.ru")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("wrong_password")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, PASSWORD_ERROR_XPATH)
    except:
        assert False, "Система не показывает ошибку при неверных данных"


def test_valid_email(driver):
    """Тест 3 - Ввод правильного email при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("email@mail.ru")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
        assert False, "Система не принимает корректный email"
    except:
        pass


def test_invalid_email(driver):
    """Тест 4 - Ввод неправильного email при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("em.ail\ma.il.ru")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
    except:
        assert False, "Система не обрабатывает некорректный email"


def test_valid_phone(driver):
    """Тест 5 - Ввод правильного номера телефона при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("89825559911")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
        assert False, "Система не принимает корректный номер телефона"
    except:
        pass


def test_invalid_phone(driver):
    """Тест 6 - Ввод неправильного номера телефона при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("009825559911")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
    except:
        assert False, "Система не обрабатывает некорректный номер телефона"


def test_valid_snils(driver):
    """Тест 7 - Ввод правильного СНИЛСа при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("123-321-456 00")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
        assert False, "Система не принимает корректный СНИЛС"
    except:
        pass


def test_invalid_snils(driver):
    """Тест 8 - Ввод неправильного СНИЛСа при авторизации"""
    driver.find_element(By.ID, LOGIN_ID).send_keys("123-32-46 001")
    driver.find_element(By.ID, PASSWORD_ID).send_keys("%AS16f7!8l0")
    driver.find_element(By.XPATH, LOGIN_BTN_XPATH).click()
    time.sleep(BETWEEN_TIME)

    try:
        driver.find_element(By.XPATH, LOGIN_ERROR_XPATH)
    except:
        assert False, "Система не обрабатывает некорректный СНИЛС"


def test_autofocus(driver):
    """Тест 9 - Проверка автофокуса на странице авторизации"""
    active_element = driver.switch_to.active_element
    login_element = driver.find_element(By.ID, LOGIN_ID)

    assert active_element == login_element, "Автофокус не установлен на поле логина"


def test_forgot_password_link(driver):
    """Тест 10 - Проверка работы ссылки "Забыли пароль?" """
    driver.find_element(By.XPATH, FORGOT_PASSWORD_XPATH).click()
    time.sleep(BETWEEN_TIME)

    assert "recovery" in driver.current_url.lower(
    ), "Ссылка 'Забыли пароль?' не работает"


def test_registration_link(driver):
    """Тест 11 - Проверка работы ссылки "Зарегистрироваться" """
    driver.find_element(By.XPATH, REGISTRATION_LINK_XPATH).click()
    time.sleep(BETWEEN_TIME)

    assert "registration" in driver.current_url.lower(
    ), "Ссылка 'Зарегистрироваться' не работает"
