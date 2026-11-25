"""
FLAKY TEST DEMONSTRATION  (the Week 6 Thursday task)

A "flaky" test is one that sometimes passes and sometimes fails WITHOUT the app
changing. The usual cause: the test looks for something before the page has
finished showing it -- a timing problem, not a real bug.

To show this RELIABLY (not at the mercy of network speed), this uses a tiny
local page, slow_page.html, that adds a ".title" element after 2 seconds.

  1. test_FLAKY_bad   -> no wait: reads .title too early -> FAILS every time
  2. test_STABLE_good -> explicit wait: waits until .title is there -> PASSES

Run:  python -m pytest test_flaky_demo.py -v
Expected result: 1 failed, 1 passed -- which is the whole point of the demo.
"""
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# file:/// URL to the local slow page sitting next to this test file
SLOW_PAGE = "file:///" + os.path.join(os.path.dirname(__file__), "slow_page.html").replace("\\", "/")


# ---------------------------------------------------------------------------
# 1) THE FLAKY WAY -- what NOT to do.
#    The page shows ".title" only after 2 seconds. With no wait, the test reads
#    it immediately, before it exists, and fails. This is a bug in the TEST,
#    not the app.
# ---------------------------------------------------------------------------
@pytest.mark.flaky_demo
def test_login_FLAKY_bad(driver):
    driver.get(SLOW_PAGE)
    # No wait: the element is not on the page yet -> NoSuchElementException.
    title = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title == "Products"


# ---------------------------------------------------------------------------
# 2) THE STABLE WAY -- the fix.
#    An EXPLICIT WAIT tells Selenium: "wait up to 15s UNTIL .title shows the
#    text 'Products', then continue." It waits exactly as long as needed.
# ---------------------------------------------------------------------------
def test_login_STABLE_good(driver):
    driver.get(SLOW_PAGE)
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".title"), "Products")
    )
    assert driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
