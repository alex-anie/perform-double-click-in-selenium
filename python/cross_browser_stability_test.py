from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
)
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_cross_browser_stability():

    # Start browser (Chrome, but can be switched to Firefox/Edge)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Free Selenium test website
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    wait = WebDriverWait(driver, 15)

    # Cross-browser quirk: button may appear at slightly different times
    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )

    start_button.click()
    print("Clicked Start button… waiting for content.")

    # Cross-browser quirk:
    # Firefox and Edge sometimes release the element differently → stale element
    result_text = None
    retries = 3

    for attempt in range(retries):
        try:
            result_text = wait.until(
                EC.visibility_of_element_located((By.ID, "finish"))
            ).text
            break  # Success → exit loop

        except StaleElementReferenceException:
            print(f"Stale element issue — retrying ({attempt+1}/{retries})…")
            time.sleep(1)

    print("Final text:", result_text)

    driver.quit()

if __name__ == "__main__":
    test_cross_browser_stability()
