import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_site():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bootcoding.hireskilldev.com/settings/profile")
    time.sleep(2)
    
    assert "Hiring" in driver.title or "Bootcoding" in driver.title
    driver.quit()
