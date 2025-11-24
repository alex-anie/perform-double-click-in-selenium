from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # STEP 1 — Visit OpenStreetMap
    driver.get("https://www.openstreetmap.org/")
    wait = WebDriverWait(driver, 15)

    # STEP 2 — Wait for the map container
    map_area = wait.until(EC.presence_of_element_located((By.ID, "map")))
    print("Map loaded.")

    # STEP 3 — Create ActionChains instance
    actions = ActionChains(driver)

    # STEP 4 — Perform a double-click using offset inside the map element
    # Coordinates: (100, 150) — You may adjust
    actions.move_to_element_with_offset(map_area, 300, 200).double_click().perform()
    print("Double-click with offset performed successfully.")

    # STEP 5 — Wait briefly to observe zoom effect
    time.sleep(3)

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
