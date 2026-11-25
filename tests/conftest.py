"""
Shared test setup (fixtures) for all tests.

A 'fixture' is code pytest runs before/after each test. The `driver` fixture
opens a browser before every UI test and closes it afterwards, so each test
starts clean. The `api` fixture gives API tests a ready-made API client.
"""
import glob
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from framework.config import HEADLESS
from framework.api_client import ApiClient


def _find_chromedriver():
    """
    Use the ChromeDriver already cached by Selenium Manager, so tests never
    pause to download it mid-run (that was causing random failures offline).
    Falls back to letting Selenium find it if the cache isn't there.
    """
    pattern = os.path.join(
        os.path.expanduser("~"),
        ".cache", "selenium", "chromedriver", "*", "*", "chromedriver.exe",
    )
    hits = glob.glob(pattern)
    return hits[0] if hits else None


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    # CI runs on a server with no screen, so config turns on headless there.
    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    path = _find_chromedriver()
    service = Service(executable_path=path) if path else Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(0)  # we use EXPLICIT waits instead (best practice)
    yield driver               # the test runs here
    driver.quit()              # cleanup after the test, pass or fail


@pytest.fixture
def api():
    """A ready-to-use API client for the REST tests."""
    return ApiClient()
