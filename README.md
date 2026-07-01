# Playwright + Python Automation Framework (Demo)

A minimal but production-shaped SDET framework built for interview demo purposes —
Page Object Model, UI tests, API tests, pytest fixtures, HTML/Allure-style reporting,
and a GitHub Actions CI/CD pipeline.

## Stack
- **Playwright (Python)** — browser automation
- **pytest** — test runner, fixtures, parametrization (data-driven testing)
- **requests** — API testing layer
- **pytest-html** — reporting (swap for Allure in a real enterprise setup)
- **GitHub Actions** — CI/CD pipeline with quality gate

## Structure
```
playwright-demo-framework/
├── pages/                  # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── ui/                 # UI regression tests (saucedemo.com — public demo site)
│   │   ├── test_login.py
│   │   └── test_inventory.py
│   └── api/                # API tests (reqres.in — public demo API)
│       └── test_api_users.py
├── utils/
│   └── config.py           # environment/config management
├── conftest.py              # fixtures (browser, page, api client)
├── pytest.ini
├── requirements.txt
└── .github/workflows/ci.yml # CI/CD pipeline
```

## Why this structure (talking points for interview)
- **POM** keeps locators/actions out of test logic → one place to fix when UI changes.
- **conftest.py fixtures** give clean setup/teardown per test, scoped per function to avoid state leakage.
- **Data-driven tests** via `pytest.mark.parametrize` — same test logic, multiple datasets.
- **Config layer** (`utils/config.py`) separates environment (base URL, credentials, headless flag)
  from test code — same suite runs against dev/stage/prod by changing one variable/env var.
- **CI/CD** runs on every push/PR, installs Playwright browsers in CI, runs tests headless,
  publishes an HTML report as a build artifact, and **fails the build (quality gate)** if any test fails.

## Run locally
```bash
pip install -r requirements.txt
playwright install --with-deps chromium
pytest -v --html=report.html --self-contained-html
```

## Extending this into the Bhavna Corp JD scope
- Swap `requests` API layer for full **Postman/Newman** collection runs in CI for contract testing.
- Add **k6** or **JMeter** performance scripts triggered as a separate CI job on the same pipeline (see notes in ci.yml).
- Add a **GitLab CI** mirror of the GitHub Actions pipeline (same stages: install → lint → test → report → gate).
- Add a `pages/` → `components/` split for reusable widgets (headers, modals) as the suite scales — same pattern as your Functionize POM work, just framework-agnostic.
