import pytest
import requests
from playwright.sync_api import sync_playwright

from utils.config import Config


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=Config.HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Fresh browser context + page per test — avoids state leaking between tests
    (cookies, localStorage, cart state etc.), same principle as isolating test data
    in a data-driven regression suite.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()
