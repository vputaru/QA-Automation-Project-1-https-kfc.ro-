"""
Test Case: Verify the "Bucuresti" button leads to the correct webpage.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_contact_button_navigation():
    service = Service()
    driver = webdriver.Chrome(service=service)

    driver.get("https://kfc.ro")

    wait = WebDriverWait(driver, 10)

    contact_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/restaurante/bucuresti"]'))
    )
    contact_button.click()

    wait.until(EC.url_to_be("https://kfc.ro/restaurante/bucuresti"))

    current_url = driver.current_url
    expected_url = "https://kfc.ro/restaurante/bucuresti"

    assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    driver.quit()
