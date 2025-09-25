import pytest
from pages.create_account_page import CreateAccountPage
import time

def test_create_account_valid(browser):
    page = CreateAccountPage(browser)
    page.load()
    page.enter_company_name("HireSkill AI")
    time.sleep(2)
    page.enter_company_email("atulthakre511@gmail.com")
    time.sleep(2)
    page.click_send_otp()
    time.sleep(60)
    # Assertion: check if redirected or OTP message shown
    assert "verify" in browser.page_source.lower()
    

def test_create_account_invalid_email(browser):
    page = CreateAccountPage(browser)
    page.load()
    page.enter_company_name("HireSkill AI")
    page.enter_company_email("invalid-email")
    page.click_send_otp()

    # Assertion: error message should be visible
    assert "invalid email" in browser.page_source.lower()
