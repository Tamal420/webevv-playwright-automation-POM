
#import playwright
#import playwright.sync_api
# import playwright.sync_api
from playwright.sync_api import Page, expect
class PatientPage:

    def __init__(self, page: playwright.sync_api.Page):
        self.page = page

    def create_patient(self):
        page = self.page

        page.get_by_role("link", name=" Patients").click()
        page.get_by_role("button", name=" Add New Patient").click()

        page.get_by_role("textbox", name="First Name *").fill("Tamal")
        page.get_by_role("textbox", name="Last Name *").fill("Saha")

        page.locator("#phoneNumber").fill("(016) 708-67710")

        page.get_by_role("textbox", name="Member/Insurance ID Number *").fill("123456789")
        page.get_by_role("textbox", name="Medical Code *").fill("T1019")

        page.get_by_role("textbox", name="Enter address").fill("New")
        page.get_by_text("New York, NY, USA", exact=True).click()

        page.get_by_role("combobox", name="Select Gender").click()
        page.get_by_text("Male", exact=True).click()

        page.locator("input[name='dateOfBirth']").click()
        page.get_by_text("1").first.click()

        page.get_by_role("textbox", name="Contact Person Name *").fill("Rahul")
        page.get_by_role("textbox", name="Contact Person Phone *").fill("(017) 114-75090")

        page.get_by_role("combobox", name="Select Insurance").click()
        page.get_by_text("Aetna Better Health Premier").click()

        page.get_by_role("combobox", name="Monthly").click()
        page.get_by_label("Option List").get_by_text("Monthly").click()

        page.get_by_role("combobox", name="Select County").click()
        page.get_by_text("Bangladesh").click()

        # page.get_by_text("English").click()
        # page.get_by_label("Options List").get_by_text("English", exact=True).click()

        page.get_by_role("combobox", name="Start Date *").click()
        page.get_by_role("button", name="Previous Month").click()
        page.get_by_role("button", name="Previous Month").click()
        page.get_by_text("1", exact=True).click()

        page.get_by_role("combobox", name="End Date *").click()
        page.get_by_text("31", exact=True).click()

        page.get_by_role("textbox", name="Name *", exact=True).fill("Foisal")
        page.locator("#caseWorkerPhoneNumber").fill("(016) 708-6771")

        page.get_by_role("textbox", name="Email *").fill("tamal890@gmail.com")

        page.get_by_role("spinbutton", name="Total Units (1 unit = 15").fill("320")
        page.get_by_role("spinbutton", name="Per Unit Cost *").fill("6.75")

        page.get_by_role("button", name="Add Weekly Task").click()

        page.get_by_text("Select Task Type").click()
        page.get_by_text("Medication").click()

        page.get_by_role("combobox", name="Select Days/Week").click()
        page.get_by_text("7 Days").click()

        page.get_by_role("button", name="Save").click()
        page.get_by_role("button", name="Yes").click()
        # Patient List Page load wait
        page.wait_for_load_state("networkidle")

        # verify patient list page loaded
        # playwright.sync_api.expect(page.get_by_role("button", name=" Add New Patient")).to_be_visible()
        expect(page.get_by_role("button", name=" Add New Patient")).to_be_visible()
        print("Patient created successfully")
    
        '''
from playwright.sync_api import Page, expect


class PatientPage:

    def __init__(self, page: Page):
        self.page = page

    def create_patient(self):

        page = self.page

        page.get_by_role("link", name=" Patients").click()

        page.wait_for_load_state("networkidle")

        page.get_by_role("button", name=" Add New Patient").click()

        page.wait_for_load_state("networkidle")

        page.get_by_role("textbox", name="First Name *").fill("Tamal")
        page.get_by_role("textbox", name="Last Name *").fill("Saha")

        page.locator("#phoneNumber").fill("(016) 708-67710")

        page.get_by_role("textbox", name="Member/Insurance ID Number *").fill("123456789")

        page.get_by_role("textbox", name="Medical Code *").fill("T1019")

        page.get_by_role("textbox", name="Enter address").fill("New")
        page.get_by_text("New York, NY, USA").click()

        # page.get_by_role("combobox", name="Select Gender").click()
        # page.get_by_text("Male").click()
        page.get_by_role("combobox", name="Select Gender").click()
        page.get_by_text("Male", exact=True).click()

        page.locator("input[name='dateOfBirth']").click()
        page.get_by_text("1").first.click()

        page.get_by_role("textbox", name="Contact Person Name *").fill("Rahul")
        page.get_by_role("textbox", name="Contact Person Phone *").fill("(017) 114-75090")

        page.get_by_role("combobox", name="Select Insurance").click()
        page.get_by_text("Aetna Better Health Premier").click()

        # page.get_by_role("combobox", name="Monthly").click()
        # page.get_by_text("Monthly").click()
        page.get_by_role("combobox", name="Monthly").click()
        page.get_by_label("Option List").get_by_text("Monthly").click()

        page.get_by_role("combobox", name="Select County").click()
        page.get_by_text("Bangladesh").click()

        page.get_by_role("combobox", name="Start Date *").click()
        page.get_by_text("1", exact=True).click()

        page.get_by_role("combobox", name="End Date *").click()
        page.get_by_text("31", exact=True).click()

        page.get_by_role("textbox", name="Name *", exact=True).fill("Foisal")

        page.locator("#caseWorkerPhoneNumber").fill("(016) 708-6771")

        page.get_by_role("textbox", name="Email *").fill("tamal890@gmail.com")

        page.get_by_role("spinbutton", name="Total Units (1 unit = 15").fill("320")

        page.get_by_role("spinbutton", name="Per Unit Cost *").fill("6.75")

        page.get_by_role("button", name="Add Weekly Task").click()

        page.get_by_text("Select Task Type").click()
        page.get_by_text("Medication").click()

        page.get_by_role("combobox", name="Select Days/Week").click()
        page.get_by_text("7 Days").click()

        page.get_by_role("button", name="Save").click()

        page.get_by_role("button", name="Yes").click()

        page.wait_for_load_state("networkidle")

        expect(page.get_by_role("button", name=" Add New Patient")).to_be_visible()

        print("Patient created successfully")
        '''