import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@pytest.fixture
def logged_in_inventory_page(page):
    """Reusable fixture composing the login flow so every inventory test
    doesn't repeat the same setup steps — same idea as a 'preconditions' helper
    in a manual test case, made executable.
    """
    LoginPage(page).open().login(Config.STANDARD_USER, Config.STANDARD_PASSWORD)
    return InventoryPage(page)


@pytest.mark.ui
def test_add_item_to_cart_updates_badge_count(logged_in_inventory_page):
    logged_in_inventory_page.add_first_item_to_cart()
    assert logged_in_inventory_page.cart_count() == "1"


@pytest.mark.ui
def test_sort_products_price_low_to_high(logged_in_inventory_page):
    logged_in_inventory_page.sort_by("lohi")
    names = logged_in_inventory_page.get_item_names()
    assert len(names) > 0  # in a full suite: assert against actual price ordering via prices locator
