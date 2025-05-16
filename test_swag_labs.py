import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwagLabsTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")

        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")))
        print("Авторизация успешна")

    def add_item_to_cart(self, item_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for item in items:
            item_title = item.find_element(
                By.CLASS_NAME, "inventory_item_name").text
            if item_title == item_name:
                add_button = item.find_element(
                    By.CSS_SELECTOR, "button.btn_inventory")
                add_button.click()
                print(f"Товар '{item_name}' добавлен в корзину")
                break

        cart_badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "Товар не был добавлен в корзину"

    def go_to_cart(self):
        cart_link = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")))
        print("Переход в корзину выполнен")

    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")))
        print("Начало оформления заказа")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        print("Данные для доставки заполнены")

    def complete_purchase(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")))
        success_message = self.driver.find_element(
            By.CLASS_NAME, "complete-header").text

        assert "Thank you for your order!" == success_message, "Покупка не была успешно завершена"
        print("Покупка успешно завершена!")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Браузер закрыт")

    def run_test(self):
        try:
            self.login("standard_user", "secret_sauce")
            time.sleep(3)
            self.add_item_to_cart("Sauce Labs Backpack")
            time.sleep(3)
            self.go_to_cart()
            time.sleep(3)
            self.checkout()
            time.sleep(3)
            self.fill_checkout_info("Elisey", "Sokolov", "12345")
            time.sleep(3)
            self.complete_purchase()
            time.sleep(3)
            print("Тест успешно пройден!")
            return True
        except Exception as e:
            print(f"Ошибка во время тестирования: {e}")
            return False
        finally:
            self.close_browser()


if __name__ == "__main__":
    test = SwagLabsTest()
    test.run_test()
