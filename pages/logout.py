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
       '''
from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.profile_btn = page.get_by_role("button").filter(has_text="Profile")
        self.logout_link = page.locator("a").filter(has_text="Logout")

    def logout(self):
        # 1. Click the profile button
        self.profile_btn.click()
        
        # 2. Wait until the logout option becomes visible (industry standard)
        self.logout_link.wait_for(state="visible", timeout=5000)
        
        # 3. Click logout
        self.logout_link.click()
        
        # 4. Verification: ensure it returned to the login page
        # Here it checks whether 'auth/login' exists in the URL
        self.page.wait_for_url("**/auth/login")
        
        # Check confirmation (optional but professional)
     
        expect(self.page).to_have_url("https://d2abiysw3nt2tr.cloudfront.net/auth/login")
        print("Logout successful")