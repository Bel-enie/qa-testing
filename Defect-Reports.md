# Defect Reports — SauceDemo

**Author:** Eniola Akingbade · Week 5

Each defect is written so a developer could act on it without asking me questions. Note the difference between **severity** (how bad the impact is, set by the tester) and **priority** (how soon it should be fixed, set by the team/business).

---

## DEF-01 — Locked-out user sees no way to recover
- **Severity:** Medium
- **Priority:** Low
- **Feature:** Login
- **Environment:** Chrome, Windows 11, saucedemo.com
- **Steps to reproduce:**
  1. Go to the login page
  2. Enter `locked_out_user` / `secret_sauce`
  3. Click Login
- **Expected:** An error that also tells the user how to get unlocked (e.g. contact support).
- **Actual:** Error says the user is locked out, but gives no recovery path.
- **Why this severity/priority:** Impact is real but limited to one account state (Medium severity); it isn't blocking most users, so it can wait (Low priority).

---

## DEF-02 — Product images all identical for problem_user
- **Severity:** High
- **Priority:** High
- **Feature:** Products page
- **Environment:** Chrome, Windows 11, saucedemo.com
- **Steps to reproduce:**
  1. Log in as `problem_user` / `secret_sauce`
  2. Look at the six product images
- **Expected:** Each product shows its own correct image.
- **Actual:** All products show the same (wrong) image.
- **Why this severity/priority:** It breaks a core part of a shopping page and misleads customers about what they're buying (High severity); customer-facing and visible, so fix soon (High priority).

---

## DEF-03 — Sort order does not work for problem_user
- **Severity:** High
- **Priority:** Medium
- **Feature:** Products — sorting
- **Steps to reproduce:**
  1. Log in as `problem_user` / `secret_sauce`
  2. Change the sort dropdown to Price (low to high)
- **Expected:** Products reorder cheapest first.
- **Actual:** The order does not change.
- **Why this severity/priority:** A key feature is broken (High severity), but a shopper can still buy without sorting, so it's not the most urgent (Medium priority).

---

## DEF-04 — Checkout accepts obviously invalid postal code
- **Severity:** Low
- **Priority:** Low
- **Feature:** Checkout — your information
- **Steps to reproduce:**
  1. Add an item and start checkout
  2. Enter first name, last name, and postal code `!!!` (symbols only)
  3. Click Continue
- **Expected:** The form rejects an invalid postal code.
- **Actual:** The form accepts it and proceeds to the overview.
- **Why this severity/priority:** Weak validation, low real-world impact on a demo (Low severity), and not urgent (Low priority) — but worth noting.

---

## DEF-05 — Error message not cleared after correcting the field
- **Severity:** Medium
- **Priority:** Medium
- **Feature:** Login
- **Steps to reproduce:**
  1. Click Login with both fields empty (error appears)
  2. Type a valid username and password
  3. Observe the red error banner
- **Expected:** The error clears once the problem is fixed, or at least on the next submit.
- **Actual:** The error banner can remain visible while the user corrects the fields, which is confusing.
- **Why this severity/priority:** A usability annoyance, not a blocker (Medium severity); worth tidying in a normal sprint (Medium priority).

---

### Severity vs Priority — the one-line summary
> **Severity = how bad the bug is. Priority = how soon we fix it.** A typo in the company logo on the homepage can be *low severity but high priority* (embarrassing, very visible); a crash in a rarely used admin screen can be *high severity but low priority*.
