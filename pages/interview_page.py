from selenium.webdriver.common.by import By

class InterviewPage:
    TOPIC_SECTION = (By.ID, "interview-output")

    def __init__(self, driver):
        self.driver = driver

    def get_topics_text(self):
        return self.driver.find_element(*self.TOPIC_SECTION).text
