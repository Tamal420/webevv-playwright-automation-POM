from playwright.sync_api import Page, expect
import re

class PatientPage:
    def __init__(self, page: Page):
        self.page = page

    def create_patient(self):
        # Click Patients link from sidebar (Regex used to avoid icon issues)
        self.page.get_by_role("link", name=re.compile("Patients", re.IGNORECASE)).click()
        self.page.wait_for_load_state("networkidle")
        
        # Click Add New Patient button
        add_btn = self.page.get_by_role("button", name="Add New Patient")
        add_btn.wait_for(state="visible")
        add_btn.click()

        # 1. Personal Information
        self.page.get_by_role("textbox", name="First Name *").fill("Tamal")
        self.page.get_by_role("textbox", name="Last Name *").fill("Saha")
        self.page.locator("#phoneNumber").fill("(016) 708-67710")
        self.page.get_by_role("textbox", name="Member/Insurance ID Number *").fill("123456789")
        self.page.get_by_role("textbox", name="Medical Code *").fill("T1019")

        # 2. Address and Gender
        self.page.get_by_role("textbox", name="Enter address").fill("New")
        self.page.get_by_text("New York, NY, USA", exact=True).click()
        
        self.page.get_by_role("combobox", name="Select Gender").click()
        self.page.get_by_text("Male", exact=True).click()

        # 3. Date of Birth and Contact
        self.page.locator("input[name='dateOfBirth']").click()
        self.page.get_by_text("1").first.click()
        self.page.get_by_role("textbox", name="Contact Person Name *").fill("Rahul")
        self.page.get_by_role("textbox", name="Contact Person Phone *").fill("(017) 114-75090")

        # 4. Insurance and Pay Type
        self.page.get_by_role("combobox", name="Select Insurance").click()
        self.page.get_by_text("Aetna Better Health Premier").click()
        
        self.page.get_by_role("combobox", name="Monthly").click()
        self.page.get_by_label("Option List").get_by_text("Monthly").click()

        self.page.get_by_role("combobox", name="Select County").click()
        self.page.get_by_text("Bangladesh").click()

        # 5. Start and End Date
        self.page.get_by_role("combobox", name="Start Date *").click()
        self.page.get_by_role("button", name="Previous Month").dblclick()
        self.page.get_by_text("1", exact=True).click()

        self.page.get_by_role("combobox", name="End Date *").click()
        self.page.get_by_text("31", exact=True).click()

        # 6. Case Worker and Cost
        self.page.get_by_role("textbox", name="Name *", exact=True).fill("Foisal")
        self.page.locator("#caseWorkerPhoneNumber").fill("(016) 708-6771")
        self.page.get_by_role("textbox", name="Email *").fill("tamal890@gmail.com")
        self.page.get_by_role("spinbutton", name="Total Units").fill("320")
        self.page.get_by_role("spinbutton", name="Per Unit Cost *").fill("6.75")

        # 7. Add Task
        self.page.get_by_role("button", name="Add Weekly Task").click()
        self.page.get_by_text("Select Task Type").click()
        self.page.get_by_text("Medication").click()
        self.page.get_by_role("combobox", name="Select Days/Week").click()
        self.page.get_by_text("7 Days").click()

        # 8. Save
        self.page.get_by_role("button", name="Save").click()
        self.page.get_by_role("button", name="Yes").click()
        self.page.wait_for_load_state("networkidle")
        
        # Verification (return to patient list)
        expect(add_btn).to_be_visible()
        print("Patient created successfully")
