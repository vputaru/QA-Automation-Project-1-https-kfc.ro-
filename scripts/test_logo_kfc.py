"""
Test Case: Verify the KFC logo is visible on the homepage
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_kfc_logo_visible():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://kfc.ro")

    logo = driver.find_element(By.XPATH, '//img[@alt="kfc-romania-logo"]')
    assert logo.is_displayed(), "Logo is not visible on the homepage"

    driver.quit()