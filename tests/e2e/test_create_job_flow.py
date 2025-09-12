import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_site():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bootcoding.hireskilldev.com/job/create/job-rounds?step=1")
    time.sleep(2)
    
    assert "Hiring" in driver.title or "Bootcoding" in driver.title
    driver.quit()
