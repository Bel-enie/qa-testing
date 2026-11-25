"""
BasePage — the shared parent class for every Page Object.

Before Week 7, each page object repeated the same waiting/clicking/typing code.
A framework removes that repetition: common actions live here ONCE, and every
page (LoginPage, ProductsPage, ...) inherits them. That is the point of a
framework — write the plumbing once, reuse it everywhere.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    # --- shared actions every page can use ---

    def open(self, url):
        self.driver.get(url)
        return self

    def _visible(self, locator):
        """Wait until an element is visible, then return it (explicit wait)."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def type(self, locator, text):
        el = self._visible(locator)
        el.clear()
        el.send_keys(text)
        return self

    def click(self, locator):
        self._clickable(locator).click()
        return self

    def text_of(self, locator):
        return self._visible(locator).text

    def count(self, locator):
        return len(self.driver.find_elements(*locator))
