'''
from playwright.sync_api import Page


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        page = self.page

        page.get_by_role("button").filter(has_text="Profile").click()

        page.wait_for_timeout(2000)

        page.locator("a").filter(has_text="Logout").click()

        page.wait_for_url("**/auth/login")

        print("Logout successful")
        '''
from playwright.sync_api import Page, expect


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

    def logout(self):

        page = self.page

        page.get_by_role("button").filter(has_text="Profile").click()

        expect(page.locator("a").filter(has_text="Logout")).to_be_visible()

        page.locator("a").filter(has_text="Logout").click()

        page.wait_for_url("**/auth/login")

        print("Logout successful")