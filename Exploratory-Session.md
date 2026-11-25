# Exploratory Testing Session

**Author:** Eniola Akingbade · Week 5

Exploratory testing = investigating the app freely to find what scripted tests miss, but guided by a **charter** (a short mission) and time-boxed so it stays focused.

---

## Charter
> **Explore** the checkout flow
> **With** different users and odd inputs
> **To discover** validation gaps and confusing behaviour.

- **Time-box:** 40 minutes
- **Tester:** Eniola Akingbade
- **Build:** saucedemo.com (live)

## What I tried (test notes)
- Logged in as `standard_user` and `problem_user` to compare behaviour.
- Started checkout with an empty cart (by navigating directly) to see if it's handled.
- Entered symbols and very long strings into the postal code field.
- Used the browser Back button mid-checkout to see if the cart state survived.
- Refreshed the page on the overview step.

## Findings
| # | Observation | Turned into |
|---|---|---|
| 1 | `problem_user` shows all the same product image | DEF-02 |
| 2 | Postal code accepts symbols-only input | DEF-04 |
| 3 | Error banner lingers after fixing login fields | DEF-05 |
| 4 | Back button during checkout keeps the cart (good — no bug) | Noted as working |
| 5 | Sorting does nothing for `problem_user` | DEF-03 |

## Reflection
Scripted test cases checked the *expected* paths. Exploratory testing — poking at edges, switching users, using the Back button — is what surfaced the `problem_user` image and sort bugs. Both approaches are needed: scripted for coverage, exploratory for the surprises.
