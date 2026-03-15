from playwright.sync_api import sync_playwright
from login import LoginPage


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.login()

        page.wait_for_timeout(5000)

        browser.close()


run()