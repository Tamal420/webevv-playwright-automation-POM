from pages.login_page import LoginPage
from pages.patient_page import PatientPage
from pages.caregiver_page import CaregiverPage
from pages.appointment_page import AppointmentPage
from pages.logout import LogoutPage

def test_full_workflow(page):
    login = LoginPage(page)
    patient = PatientPage(page)
    caregiver = CaregiverPage(page)
    appointment = AppointmentPage(page)
    logout = LogoutPage(page)

    # Login
    login.login()

    # Patient create
    patient.create_patient()
    page.wait_for_selector("table tbody tr")
    page.wait_for_timeout(3000)

    # Caregiver page
    page.get_by_role("link", name="Caregiver").click()

    caregiver.create_caregiver()
    page.wait_for_selector("table tbody tr")
    page.wait_for_timeout(3000)

    # Appointment page
    page.locator("a[href='/appointments']").click()

    appointment.create_appointment()
    page.wait_for_selector("table tbody tr")
    page.wait_for_timeout(3000)

    # Invoice generate
    # appointment.generate_invoice_from_latest()

    #Logout
    logout.logout()
