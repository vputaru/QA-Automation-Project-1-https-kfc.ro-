"""
Test Case: Verify KFC page title is correct.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_open_kfc():
    service = Service()
    driver = webdriver.Chrome(service=service)

    driver.get("https://kfc.ro")
    assert "Jumătatea Nepicantă" in driver.title

    driver.quit()
