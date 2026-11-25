"""
Central configuration for the whole framework.

Keeping URLs and settings in ONE place is part of turning loose scripts into a
framework: when something moves, I change it here, not in every test file.
Values can also be overridden with environment variables, which is how a CI
server (GitHub Actions) passes settings in.
"""
import os

# The web app under test (Selenium / UI tests)
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

# The REST API under test (API tests)
API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

# How long explicit waits are allowed to wait, in seconds
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))

# Run the browser without a visible window? CI sets HEADLESS=1 so it can run
# on a server that has no screen. On your laptop it stays visible by default.
HEADLESS = os.getenv("HEADLESS", "0") == "1"

# Standard SauceDemo test accounts (documented in one place)
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"
PASSWORD = "secret_sauce"
