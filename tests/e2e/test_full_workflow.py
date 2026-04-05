import pytest
from pages.login_page import LoginPage
from pages.patient_page import PatientPage
from pages.caregiver_page import CaregiverPage
from pages.appointment_page import AppointmentPage
from pages.logout import LogoutPage

def test_full_workflow(page):
    # Create objects
    login = LoginPage(page)
    patient = PatientPage(page)
    caregiver = CaregiverPage(page)
    appointment = AppointmentPage(page)
    logout = LogoutPage(page)

    # Actual test flow (as per video)
    login.login()
    page.wait_for_load_state("networkidle")
    patient.create_patient()
    page.wait_for_load_state("networkidle")
    caregiver.create_caregiver()
    page.wait_for_load_state("networkidle")
    appointment.create_appointment()
    page.wait_for_load_state("networkidle")
    logout.logout()
    page.wait_for_load_state("networkidle")
    
