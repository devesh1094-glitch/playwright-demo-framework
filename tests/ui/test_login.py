import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login_lands_on_inventory(page):
    login_page = LoginPage(page).open()
    login_page.login(Config.STANDARD_USER, Config.STANDARD_PASSWORD)

    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()


@pytest.mark.ui
@pytest.mark.parametrize(
    "username, password, expected_error_substring",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "wrong_password", "do not match"),
        ("", "secret_sauce", "Username is required"),
    ],
)
def test_invalid_login_shows_correct_error(page, username, password, expected_error_substring):
    """Data-driven negative testing — one test body, multiple invalid credential
    scenarios, mirrors how I parametrize regression data sets in enterprise suites.
    """
    login_page = LoginPage(page).open()
    login_page.login(username, password)

    error_text = login_page.get_error_text()
    assert expected_error_substring.lower() in error_text.lower()
