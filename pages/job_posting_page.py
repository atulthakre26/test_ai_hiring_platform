from selenium.webdriver.common.by import By

class JobPostingPage:
    JOB_ROLE = (By.NAME, "jobRole")         # update locator from HTML
    EXPERIENCE = (By.NAME, "experience")    # update locator
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")
    JD_SECTION = (By.ID, "jd-output")       # placeholder

    def __init__(self, driver):
        self.driver = driver

    def enter_job_role(self, role):
        self.driver.find_element(*self.JOB_ROLE).send_keys(role)

    def enter_experience(self, exp):
        self.driver.find_element(*self.EXPERIENCE).send_keys(exp)

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def get_jd_text(self):
        return self.driver.find_element(*self.JD_SECTION).text
