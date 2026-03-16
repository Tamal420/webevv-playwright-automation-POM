'''
from playwright.sync_api import Page
import config


class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page

    def login(self):
        self.page.goto(config.BASE_URL)

        self.page.get_by_role("textbox", name="User Name").fill(config.USERNAME)

        self.page.get_by_role("textbox", name="Password").fill(config.PASSWORD)

        self.page.get_by_role("button", name="SIGN IN").click()
        self.page.wait_for_load_state("networkidle")
 '''
'''
from playwright.sync_api import Page, expect
import config


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def login(self):

        self.page.goto(config.BASE_URL)

        self.page.get_by_role("textbox", name="User Name").fill(config.USERNAME)
        self.page.get_by_role("textbox", name="Password").fill(config.PASSWORD)

        self.page.get_by_role("button", name="SIGN IN").click()

        # wait dashboard load
        self.page.wait_for_load_state("networkidle")

        expect(self.page.get_by_role("button").filter(has_text="Profile")).to_be_visible()

        print("Login successful")
        '''
from playwright.sync_api import Page, expect
import config

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="User Name")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signin_button = page.get_by_role("button", name="SIGN IN")
        self.profile_btn = page.get_by_role("button").filter(has_text="Profile")

    def login(self):
        self.page.goto(config.BASE_URL)
        self.username_input.fill(config.USERNAME)
        self.password_input.fill(config.PASSWORD)
        self.signin_button.click()
        self.page.wait_for_load_state("networkidle")
        # Profile button visible that indicates successful login 
        expect(self.profile_btn).to_be_visible(timeout=10000)
        print("Login successful")