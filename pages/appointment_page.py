import re
from playwright.sync_api import Page, expect
class AppointmentPage:
    def __init__(self, page: Page):
        self.page = page
    def create_appointment(self):   
        #Clicking from the sidebar
        #self.page.get_by_role("link", name=re.compile("Appointment", re.IGNORECASE)).click()
        self.page.locator("a[href='/appointments']").click()
        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("button", name="Add new Appointment").click()
        #1st patient selects from the dropdown
        #self.page.locator("select[name='patient']").select_option(index=1)
        #self.page.locator("select[name='caregiver']").select_option(index=1)
        #self.page.locator("div").filter(has_text=re.compile(r"^Select Patient \*$")).click()
        #self.page.locator("div.ant-select-item-option-content").first.click()


        #self.page.locator("div").filter(has_text=re.compile(r"^Assign Caregiver \*$")).click()
        #self.page.locator("div.ant-select-item-option-content").first.click()
        patient_dropdown = self.page.locator("p-dropdown[formcontrolname='patientId']")
        patient_dropdown.wait_for(state="visible", timeout=10000)
        patient_dropdown.click()

        #First option selection-patient
        self.page.locator("p-dropdownitem").first.click()

        caregiver_dropdown = self.page.locator("p-dropdown[formcontrolname='caregiverId']")
        caregiver_dropdown.wait_for(state="visible", timeout=10000)
        caregiver_dropdown.click()
        #First option selection-caregiver
        self.page.locator("p-dropdownitem").first.click()

        #Date and time selection
        self.page.get_by_label("Start Date").click()
        self.page.get_by_label("Start Date").fill("01-01-2026")
        self.page.get_by_label("End Date").click()
        self.page.get_by_label("End Date").fill("08-31-2026")
        self.page.get_by_label("Task Start Time").click()
        self.page.get_by_label("Task Start Time").fill("07:00 AM")

        #Auto clock In enables
        self.page.get_by_label("Enable auto clock in").check()
        #Clicks the create button
        self.page.get_by_role("button", name="Create").click()

        #Wait for the appointment to be created and the page to load
        self.page.wait_for_url(re.compile(".*schedule.*"))
        self.page.wait_for_load_state("networkidle")
        #print("Appointment created successfully!")
        print("Appointment workflow completed and redirected to schedule list.")
