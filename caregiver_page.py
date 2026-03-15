from playwright.sync_api import Page, expect


class CaregiverPage:

    def __init__(self, page: Page):
        self.page = page

    def create_caregiver(self):

        page = self.page

        page.get_by_role("link", name=" Caregiver").click()

        page.wait_for_load_state("networkidle")

        expect(page.get_by_role("button", name=" Add New Caregiver")).to_be_visible()

        page.get_by_role("button", name=" Add New Caregiver").click()

        page.wait_for_load_state("networkidle")

        page.get_by_role("textbox", name="First Name *").fill("Stonis")
        page.get_by_role("textbox", name="Last Name *").fill("Steve")
        page.get_by_role("textbox", name="User Name *").fill("stonis123")
        page.get_by_role("textbox", name="Password *", exact=True).fill("12345678")
        page.get_by_role("textbox", name="Confirm Password *").fill("12345678")

        # page.locator("#gender").get_by_role("combobox").click()
        #page.get_by_text("Male").click()
        page.locator("#gender").get_by_role("combobox").click()
        page.get_by_text("Male", exact=True).click()

        page.get_by_role("button", name="Choose Date").first.click()
        page.get_by_text("1").first.click()

        page.get_by_role("textbox", name="Phone Number *").fill("(167) 086-7710")

        page.get_by_role("combobox", name="Date Hired *").click()
        page.get_by_text("2").nth(1).click()

        page.get_by_role("textbox", name="Email *").fill("stonis564@gmail.com")

        page.get_by_role("textbox", name="Social Security Number *").fill("567-81-2340")

        page.get_by_role("textbox", name="Champ's ID Number *").fill("76542092")
        page.get_by_role("spinbutton", name="Caregiver's Rate *").fill("20")

        page.get_by_role("textbox", name="Enter address").fill("New")
        page.get_by_text("New York, NY, USA").click()

        page.get_by_role("textbox", name="Apartment/Suite/Unit").fill("22A")

        page.locator("#weeklyAvailabilities").get_by_role("combobox").click()

        page.get_by_text("Saturday").click()
        page.get_by_text("Sunday").click()
        page.get_by_text("Monday").click()
        page.get_by_text("Tuesday").click()
        page.get_by_text("Wednesday").click()
        page.get_by_text("Thursday").click()
        page.get_by_text("Friday").click()

        page.get_by_role("checkbox", name="Available for 24 hours").check()
        page.get_by_role("checkbox", name="Manage Clock In/Out").check()

        page.get_by_role("button", name="Save Caregiver").click()

        page.wait_for_load_state("networkidle")

        expect(page.get_by_role("button", name=" Add New Caregiver")).to_be_visible()

        print("Caregiver created successfully")