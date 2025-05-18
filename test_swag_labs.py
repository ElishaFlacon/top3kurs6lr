import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)


def test_driver_start(driver):
    driver.get("https://www.saucedemo.com/")


def test_login(driver, wait):
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("Авторизация успешна")

    time.sleep(3)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_add_item_to_cart(driver, wait):
    item_name = "Sauce Labs Backpack"
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    for item in items:
        item_title = item.find_element(
            By.CLASS_NAME, "inventory_item_name").text
        if item_title == item_name:
            add_button = item.find_element(
                By.CSS_SELECTOR, "button.btn_inventory")
            add_button.click()
            print(f"Товар '{item_name}' добавлен в корзину")
            break

    time.sleep(3)

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Товар не был добавлен в корзину"


def test_go_to_cart(driver, wait):
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    print("Переход в корзину выполнен")

    time.sleep(3)

    assert driver.current_url == "https://www.saucedemo.com/cart.html"


def test_checkout(driver, wait):
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    print("Начало оформления заказа")

    time.sleep(3)

    assert "checkout-step-one" in driver.current_url


def test_fill_checkout_info(driver, wait):
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Elisey")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Sokolov")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("12345")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    print("Данные для доставки заполнены")

    time.sleep(3)

    assert "checkout-step-two" in driver.current_url


def test_complete_purchase(driver, wait):
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header"))
    )
    success_message = driver.find_element(
        By.CLASS_NAME,
        "complete-header"
    ).text

    assert "Thank you for your order!" == success_message, "Покупка не была успешно завершена"

    time.sleep(3)

    assert "checkout-complete" in driver.current_url
