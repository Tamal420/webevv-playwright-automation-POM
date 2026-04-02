import re
from playwright.sync_api import Page

class AppointmentPage:
    def __init__(self, page: Page):
        self.page = page

    def create_appointment(self):  
        # Navigate
        self.page.locator("a[href='/appointments']").click()
        self.page.wait_for_load_state("networkidle")

        self.page.get_by_role("button", name="Add new Appointment").click()
        self.page.wait_for_load_state("networkidle")

        # Patient
        patient_dropdown = self.page.locator("#patientPicker")
        self.page.wait_for_function("""
        () => {
            const el = document.querySelector('#patientPicker');
            return el && el.getAttribute('aria-disabled') === 'false';
        }
        """)
        patient_dropdown.click(force=True)
        self.page.locator(".p-select-option").first.click()
        print("Patient Selected")

        # Caregiver
        caregiver_dropdown = self.page.locator("p-select").nth(1)
        caregiver_dropdown.click(force=True)
        self.page.locator(".p-select-option").first.click()
        print("Caregiver Selected")

        # Generate dates
   
        #Start Date
        start_input = self.page.locator("#appointmentStartDate input")
        start_input.wait_for(state="visible")
        start_input.click()

        self.page.get_by_role("button", name="Previous Month").click()
        self.page.wait_for_timeout(300)
        self.page.locator(".p-datepicker-day:not(.p-datepicker-other-month):has-text('1')").first.click()
        #End date
        # Auto clock in
        checkbox = self.page.get_by_label("Enable auto clock in")
        if not checkbox.is_checked():
            checkbox.check()
        print("Auto Clock Enabled")
        # Create
        self.page.get_by_role("button", name="Create").click()
        
        #self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)  # small buffer (UI settle)
        self.page.wait_for_timeout(2000)  # small buffer (UI settle)
        self.page.wait_for_selector("table, .p-datatable", timeout=30000)
        print("Navigated to Appointment List Page")
        
        
        
        
        
        

       


