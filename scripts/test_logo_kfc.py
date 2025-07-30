"""
Test Case: Verify the KFC logo is visible on the homepage
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://kfc.ro/")

logo = driver.find_element(By.XPATH, '//img[@alt="kfc-romania-logo"]')

assert logo.is_displayed(), "Logo is not visible on the homepage"

print("Logo is visible on the homepage.")

driver.quit()
