from selenium.webdriver.common.by import By

class ScreeningPage:
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")
    SCREENING_SECTION = (By.ID, "screening-output")

    def __init__(self, driver):
        self.driver = driver

    def get_screening_text(self):
        return self.driver.find_element(*self.SCREENING_SECTION).text

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
