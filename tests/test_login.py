"""
Automated login tests for SauceDemo.
These mirror the manual test cases TC-01..TC-07 from Week 5.
Each test ends with an ASSERT — the line that decides pass or fail.
"""
import pytest
from framework.pages import LoginPage, ProductsPage


def test_valid_login_shows_products(driver):
    """TC-01: a valid user reaches the products page."""
    LoginPage(driver).load().login("standard_user", "secret_sauce")
    assert ProductsPage(driver).is_loaded(), "Products page should load after valid login"


def test_locked_out_user_is_blocked(driver):
    """TC-02: the locked-out user gets a clear error."""
    login = LoginPage(driver).load()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_text().lower()


def test_wrong_password_is_rejected(driver):
    """TC-03: wrong password is refused."""
    login = LoginPage(driver).load()
    login.login("standard_user", "wrong_password")
    assert "do not match" in login.error_text().lower()


def test_empty_username_is_required(driver):
    """TC-05: empty username is caught."""
    login = LoginPage(driver).load()
    login.login("", "secret_sauce")
    assert "username is required" in login.error_text().lower()


def test_empty_password_is_required(driver):
    """TC-06: empty password is caught."""
    login = LoginPage(driver).load()
    login.login("standard_user", "")
    assert "password is required" in login.error_text().lower()


# A data-driven test: one test function, several inputs. pytest runs it once per row.
@pytest.mark.parametrize("username,password,expected", [
    ("", "", "username is required"),
    ("standard_user", "", "password is required"),
    ("", "secret_sauce", "username is required"),
])
def test_login_field_validation(driver, username, password, expected):
    """TC-05..07 as a decision table, checked in one parametrized test."""
    login = LoginPage(driver).load()
    login.login(username, password)
    assert expected in login.error_text().lower()
