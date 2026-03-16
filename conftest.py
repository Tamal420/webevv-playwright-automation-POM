# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()