"""
Product and cart tests — mirror manual cases TC-09, TC-14, TC-16.
Shows: logging in as a precondition, counting elements, and cart actions.
"""
import pytest
from framework.pages import LoginPage, ProductsPage


@pytest.fixture
def logged_in(driver):
    """A fixture that logs in first, so each product test starts on the products page."""
    LoginPage(driver).load().login("standard_user", "secret_sauce")
    products = ProductsPage(driver)
    assert products.is_loaded()
    return products


def test_six_products_are_listed(logged_in):
    """TC-09: exactly six products after login."""
    assert logged_in.product_count() == 6


def test_add_backpack_updates_cart_badge(logged_in):
    """TC-14: adding an item shows 1 on the cart badge."""
    assert logged_in.cart_count() == 0          # starts empty
    logged_in.add_backpack_to_cart()
    assert logged_in.cart_count() == 1          # now one item
