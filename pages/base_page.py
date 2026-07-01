from playwright.sync_api import Page, expect


class BasePage:
    """Common, reusable actions shared by every page object.
    Concrete pages inherit this instead of duplicating waits/clicks/asserts.
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def text_of(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def assert_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def assert_text(self, locator: str, expected_text: str):
        expect(self.page.locator(locator)).to_have_text(expected_text)
