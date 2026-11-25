# QA Testing

**Eniola Akingbade · Software Testing Internship (Phase 2)**

A software-testing project built across several weeks, from manual test design to
automated UI tests, API tests, and continuous integration.

- **Web app under test:** [SauceDemo](https://www.saucedemo.com) — a public demo shop.
- **API under test:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a public REST practice API.
- **Language & tools:** Python, Selenium WebDriver, PyTest, Requests.

---

## What's in this project

### Test design (Week 5)
- `Test-Plan.md` — scope, approach and techniques
- `Test-Cases.xlsx` — 28 test cases, tagged by technique
- `Defect-Reports.md` — 5 defect reports (severity vs priority)
- `Exploratory-Session.md` — an exploratory testing charter and findings

### Automated tests (Week 6)
- `tests/test_login.py` — Selenium login tests + a data-driven test
- `tests/test_products.py` — product and cart tests
- `tests/test_flaky_demo.py` — a flaky test and its fix (explicit waits)

### Framework, API testing & CI (Week 7)
- `framework/` — a Page Object framework (shared base page, config, API client)
- `tests/test_api.py` — API tests: GET/POST/PUT/DELETE, status codes, JSON schema
- `.github/workflows/tests.yml` — GitHub Actions CI that runs the API tests on every push and pull request

> The Week 7 framework, API tests and CI live on the `week7-framework-api-ci`
> branch and arrive here when that pull request is merged.

---

## How to run the tests

Install the dependencies, then run with PyTest:

```bash
pip install -r requirements.txt

# all tests
python -m pytest -v

# just the login tests (opens a browser)
python -m pytest tests/test_login.py -v

# the flaky-vs-fixed demo (expect 1 failed, 1 passed — that's the point)
python -m pytest tests/test_flaky_demo.py -v
```

---

## About the application under test

SauceDemo stands in for a real application until one is assigned. The techniques,
framework, waits and assertions all carry over — only the URLs and locators change
when the real app arrives.
