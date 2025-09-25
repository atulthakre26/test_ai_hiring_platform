from selenium.webdriver.common.by import By

class CreateAccountPage:
    URL = "https://careers.hireskilldev.com/auth/signup"   # replace with your page URL

    COMPANY_NAME = (By.NAME, "companyName")  # update locator based on HTML
    COMPANY_EMAIL = (By.NAME, "companyEmail")
    SEND_OTP_BUTTON = (By.XPATH, "//button[contains(text(), 'Send OTP')]")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def enter_company_name(self, name):
        self.driver.find_element(*self.COMPANY_NAME).send_keys(name)

    def enter_company_email(self, email):
        self.driver.find_element(*self.COMPANY_EMAIL).send_keys(email)

    def click_send_otp(self):
        self.driver.find_element(*self.SEND_OTP_BUTTON).click()
