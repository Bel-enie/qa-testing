"""
Page Objects, refactored for Week 7.

Each page is now a small class that INHERITS from BasePage, so it only has to
list its own locators and the actions unique to it. All the waiting/typing/
clicking machinery comes from BasePage. This is the Page Object Model done as a
proper framework rather than as standalone scripts.
"""
from selenium.webdriver.common.by import By

from framework.base_page import BasePage
from framework.config import BASE_URL


class LoginPage(BasePage):
    # Stable locators: data-test / id attributes made for testing.
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        self.open(BASE_URL)
        self._visible(self.USERNAME)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        return self

    def error_text(self):
        return self.text_of(self.ERROR)


class ProductsPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")               # says "Products"
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def is_loaded(self):
        return self.text_of(self.TITLE) == "Products"

    def product_count(self):
        self._visible(self.INVENTORY_ITEM)
        return self.count(self.INVENTORY_ITEM)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)
        return self

    def cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0
