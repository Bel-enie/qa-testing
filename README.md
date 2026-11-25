# QA Testing — Weeks 5, 6 & 7

**Eniola Akingbade · Phase 2 · Software Testing**

- **Web app under test:** SauceDemo (https://www.saucedemo.com) — public demo shop.
- **API under test:** JSONPlaceholder (https://jsonplaceholder.typicode.com) — public REST practice API.

---

## What's here

```
QA-Testing/
├── framework/              ← the test framework (Week 7)
│   ├── config.py           base URLs + settings, in one place
│   ├── base_page.py        BasePage: shared wait/click/type for every page
│   ├── pages.py            Page Objects (LoginPage, ProductsPage)
│   └── api_client.py       API client with automatic retries
├── tests/
│   ├── conftest.py         fixtures: `driver` (browser) and `api` (API client)
│   ├── test_login.py       UI login tests + data-driven test
│   ├── test_products.py    UI product/cart tests
│   ├── test_flaky_demo.py  the flaky test + the fix (Week 6)
│   ├── test_api.py         API tests: GET/POST/PUT/DELETE, status, schema
│   └── slow_page.html      local page for the flaky demo
├── .github/workflows/tests.yml   ← CI: runs API tests on every push/PR
├── requirements.txt        dependencies
├── pytest.ini              pytest config + markers
├── Test-Plan.md            Week 5 docs ↓
├── Test-Cases.xlsx         28 test cases
├── Defect-Reports.md       5 defects
└── Exploratory-Session.md  exploratory charter + findings
```

---

## How to run the tests

```bash
# API tests only — fast, no browser (great for a quick check / CI)
python -m pytest -m api -v

# UI tests only — opens a real browser
python -m pytest -m ui -v        # or: python -m pytest tests/test_login.py -v

# everything
python -m pytest -v

# with an HTML report you can open in a browser
python -m pytest -m api --html=report.html --self-contained-html -v
```

The report lands at `report.html` — double-click to open it.

---

## The framework (Week 7)

Weeks 5–6 were loose scripts. Week 7 turns them into an **engineering project**:

- **Page Object Model** — each page is a class in `framework/pages.py`; they all
  inherit shared actions from `BasePage`, so the waiting/clicking code is written
  **once**.
- **Config in one place** — `framework/config.py` holds the URLs and settings, and
  can be overridden by environment variables (how CI passes them in).
- **API client** — `framework/api_client.py` is the API version of a Page Object:
  tests go through it instead of calling `requests` directly. It **retries**
  automatically if the network blips.

## API testing (Week 7)

`tests/test_api.py` tests the data layer directly over HTTP — faster and less
fragile than UI tests. It covers:

- **GET** (read), **POST** (create), **PUT** (update), **DELETE** (remove)
- **Status codes** — 200 OK, 201 Created, 404 Not Found
- **JSON body** checks and a **schema** check (the response's shape)
- a **data-driven** API test (one test, several ids)

## CI — GitHub Actions (Week 7)

`.github/workflows/tests.yml` runs the API tests **automatically** on every push
and every pull request. That's Continuous Integration: mistakes are caught the
moment code changes. The run uploads an HTML report you can download.

---

## When you get the REAL app
Change the URLs in `framework/config.py` and the locators in `framework/pages.py`.
The framework, API client, waits, assertions and CI all carry over unchanged.
