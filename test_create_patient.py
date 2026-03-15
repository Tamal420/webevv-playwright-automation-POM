'''
from playwright.sync_api import sync_playwright
from login import LoginPage
from patient_page import PatientPage
from logout import LogoutPage


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # page = browser.new_page()
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        patient = PatientPage(page)
        logout = LogoutPage(page)

        # Login
        login.login()

        # Create patient
        patient.create_patient()

        # Logout
        logout.logout()

        browser.close()


run()
'''
from playwright.sync_api import sync_playwright

from login import LoginPage
from patient_page import PatientPage
from caregiver_page import CaregiverPage
from logout import LogoutPage


def run():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()

        login = LoginPage(page)
        patient = PatientPage(page)
        caregiver = CaregiverPage(page)
        logout = LogoutPage(page)

        # Login
        login.login()

        # Create Patient
        patient.create_patient()

        # Create Caregiver
        caregiver.create_caregiver()

        # Logout
        logout.logout()

        browser.close()


run()