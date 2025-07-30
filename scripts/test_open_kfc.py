"""
Test Case: Verify KFC page title is correct.
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://kfc.ro/")

assert "Jumătatea Nepicantă" in driver.title, "Page title does not contain 'Jumătatea Nepicantă'"

print("KFC homepage loaded successfully with correct title:", driver.title)

driver.quit()