from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BUTTON = "button.btn_inventory"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    ITEM_NAMES = ".inventory_item_name"

    def is_loaded(self) -> bool:
        return self.text_of(self.PAGE_TITLE) == "Products"

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()
        return self

    def cart_count(self) -> str:
        return self.text_of(self.CART_BADGE)

    def sort_by(self, option_value: str):
        self.page.locator(self.SORT_DROPDOWN).select_option(option_value)
        return self

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()
