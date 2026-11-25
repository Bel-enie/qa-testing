# Test Plan — SauceDemo Web Application

**Author:** Eniola Akingbade
**Phase 2 · Software Testing · Week 5**
**Application under test:** SauceDemo — https://www.saucedemo.com (standing in for the real app until it is assigned)

---

## 1. Purpose
This plan describes how I will test the SauceDemo web application: what I will test, the techniques I will use, and how I will report what I find. The goal is to design tests properly — using recognised techniques — rather than clicking around at random.

## 2. Scope

**In scope**
- Login (valid, invalid, locked-out user, empty fields)
- Products page (listing, sorting, add/remove from cart)
- Cart (contents, quantity, continue/checkout)
- Checkout (customer information, validation, order completion)

**Out of scope**
- Performance and load testing
- Security/penetration testing
- Mobile browsers (desktop Chrome only this week)

## 3. Test approach
I design test cases with three formal techniques, then add exploratory testing on top:

| Technique | Where I use it |
|---|---|
| **Equivalence partitioning** | Login fields — split inputs into valid / invalid groups and test one from each |
| **Boundary value analysis** | Checkout postal code and cart quantities — test the edges (empty, min, max) |
| **Decision tables** | Login — combinations of username present/absent × password present/absent |
| **Exploratory testing** | A timed, charter-led session to find what scripted tests miss |

## 4. Test levels
- **System testing** — testing the whole running application through the browser (my main focus).
- (Unit and integration testing would be done by developers; noted for completeness.)

## 5. Environment
- Windows 11, Google Chrome (latest)
- Application: https://www.saucedemo.com
- Test data: the accepted users listed on the login page (e.g. `standard_user`, `locked_out_user`), password `secret_sauce`

## 6. Deliverables
- This test plan
- 25+ test cases (spreadsheet)
- 5+ defect reports (severity vs priority)
- One exploratory testing session with a charter and findings

## 7. Entry / exit criteria
- **Entry:** application is reachable; test data is available.
- **Exit:** all planned test cases executed; defects logged; results summarised for the Friday presentation.

## 8. Risks
- SauceDemo is a demo app with deliberately "buggy" users — some defects are intentional, which is useful for practice.
- The real application under test may differ; techniques carry over even if the specific cases change.
