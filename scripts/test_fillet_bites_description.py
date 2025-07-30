"""
Test Case: Verify the description of the Fillet Bites product.
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
        EC.element_to_be_clickable((By.XPATH, '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))
    )
    contact_button.click()

    contact_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="products-url svelte-puytqi"]'))
    )
    contact_button.click()

    contact_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//swiper-slide[@data-swiper-slide-slug="pui"]'))
    )
    contact_button.click()

    contact_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/meniu/pui/fillet-bites" and @class="svelte-1wmiqkp"]'))
    )
    contact_button.click()

    wait.until(EC.url_to_be("https://kfc.ro/meniu/pui/fillet-bites"))

    description_element = driver.find_element(By.XPATH, '//div[@class="product-description svelte-1b1ksgq"]')
    
    actual_text = description_element.text
    expected_text = """Fillet Bites®, bucăți fresh de pui, nepicante, preparate în fiecare zi în bucătăriile noastre.
Alege între 6 sau 9 Fillet Bites®."""

    assert actual_text == expected_text, f"Incorrect description.\nExpected: {expected_text}\nGot: {actual_text}"

    driver.quit()