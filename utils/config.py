import os


class Config:
    """Centralized environment config — one switch to change target environment.
    In CI this is set via GitHub Actions 'env:' or repo secrets, never hardcoded.
    """

    ENV = os.getenv("TEST_ENV", "staging")

    BASE_URLS = {
        "staging": "https://www.saucedemo.com",
        "prod": "https://www.saucedemo.com",
    }

    API_BASE_URLS = {
        "staging": "https://reqres.in/api",
        "prod": "https://reqres.in/api",
    }

    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

    STANDARD_USER = os.getenv("TEST_USER", "standard_user")
    STANDARD_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")

    @classmethod
    def base_url(cls):
        return cls.BASE_URLS[cls.ENV]

    @classmethod
    def api_base_url(cls):
        return cls.API_BASE_URLS[cls.ENV]
