import pytest
from pages.login_page import LoginPage
from pages.patient_page import PatientPage
from pages.caregiver_page import CaregiverPage
from pages.logout import LogoutPage

def test_webevv_automation_cycle(page):
    # Create objects
    login = LoginPage(page)
    patient = PatientPage(page)
    caregiver = CaregiverPage(page)
    logout = LogoutPage(page)

    # Actual test flow (as per video)
    login.login()
    patient.create_patient()
    caregiver.create_caregiver()
    logout.logout()