import re
import sys
#from datetime import datetime
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import Page, expect
from utils import get_human_first_name, get_human_last_name, get_human_username, get_random_digits

class CaregiverPage:
    def __init__(self, page: Page):
        self.page = page

    def create_caregiver(self):
        # Navigate to Caregiver menu
        # self.page.get_by_role("link", name=re.compile("Caregiver", re.IGNORECASE)).click()
        self.page.get_by_role("link", name=re.compile("Caregiver", re.IGNORECASE)).first.click()
        self.page.wait_for_load_state("networkidle")
        
        add_btn = self.page.get_by_role("button", name=re.compile("Add New Caregiver", re.IGNORECASE))
        add_btn.click()

        # Basic information
    
        self.page.get_by_label("First Name").fill(get_human_first_name())
        self.page.get_by_label("Last Name").fill(get_human_last_name())
        self.page.get_by_label("User Name").fill(get_human_username())
        self.page.get_by_role("textbox", name="Password *", exact=True).fill("12345678")
        self.page.get_by_role("textbox", name="Confirm Password *").fill("12345678")

        # Gender and date
        self.page.locator("#gender").click()
        self.page.get_by_text("Male", exact=True).click()
        #DOB
        dob_input = self.page.locator("#dateOfBirth")
        dob_input.wait_for(state="visible")
        dob_input.click()
        self.page.get_by_role("button", name="Previous Month").click()
        self.page.wait_for_timeout(300)
        day_01 = self.page.locator(".p-datepicker-day:not(.p-datepicker-other-month):has-text('1')").first
        day_01.wait_for(state="visible")
        day_01.click()

        # Phone, email and ID
        #self.page.get_by_role("textbox", name="Phone Number *").fill("(167) 086-7710")
        self.page.get_by_label("Phone Number").fill(get_random_digits(10))
        date_hired_input = self.page.locator("#dateHired")
        date_hired_input.wait_for(state="visible")
        date_hired_input.click()
        self.page.get_by_role("button", name="Previous Month").click()
        self.page.wait_for_timeout(300)
        day_01 = self.page.locator(".p-datepicker-day:not(.p-datepicker-other-month):has-text('1')" ).first

        day_01.wait_for(state="visible")
        day_01.click()

        #self.page.get_by_role("textbox", name="Email *").fill("stonis564@gmail.com")
        random_user = get_human_username()
        dynamic_email = f"{random_user}{get_random_digits(3)}@gmail.com"
        self.page.get_by_role("textbox", name="Email *").fill(dynamic_email)
        #self.page.get_by_role("textbox", name="Social Security Number *").fill("567-81-2340")
        self.page.get_by_label("Social Security Number").fill(get_random_digits(9))
        self.page.get_by_role("textbox", name="Champ's ID Number *").fill("76542092")
        self.page.get_by_role("spinbutton", name="Caregiver's Rate *").fill("20")

        # Address
        self.page.get_by_role("textbox", name="Enter address").fill("New")
        self.page.get_by_text("New York, NY, USA").click()
        self.page.get_by_role("textbox", name="Apartment/Suite/Unit").fill("22A")

        # Availability (multiple days)
        self.page.locator("#weeklyAvailabilities").click()
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            self.page.get_by_text(day).click()
        self.page.keyboard.press("Escape") # Close the dropdown

        # Checkboxes and save
        self.page.get_by_role("checkbox", name="Available for 24 hours").check()
        self.page.get_by_role("checkbox", name="Manage Clock In/Out").check()
        self.page.get_by_role("button", name="Save Caregiver").click()
        
        self.page.wait_for_load_state("networkidle")
        expect(add_btn).to_be_visible()
        print("Caregiver created successfully")

        