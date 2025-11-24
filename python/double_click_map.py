from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome()

try:
    # Visit map
    driver.get("https://www.openstreetmap.org/")
    wait = WebDriverWait(driver, 15)

    # Search field
    search_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content input#query"))
    )

    # Type a country
    search_box.clear()
    search_box.send_keys("Nigeria")
    search_box.send_keys(Keys.ENTER)

    # Allow map to load
    time.sleep(5)

    # Extract initial zoom from URL
    def get_zoom_from_url(url):
        match = re.search(r"#map=(\d+)/", url)
        return int(match.group(1)) if match else None

    initial_zoom = get_zoom_from_url(driver.current_url)
    print("Initial Zoom:", initial_zoom)

    # Double-click on the map
    map_area = wait.until(EC.presence_of_element_located((By.ID, "map")))
    actions = ActionChains(driver)
    actions.double_click(map_area).perform()
    print("✔ Double-click performed")

    # Wait for zoom animation / URL update
    time.sleep(3)

    # Check zoom increased (via URL)
    new_zoom = get_zoom_from_url(driver.current_url)
    print("Zoom After Double-Click:", new_zoom)

    if new_zoom and initial_zoom and new_zoom > initial_zoom:
        print("🎉 SUCCESS — Map zoomed after double-click!")
    else:
        print("⚠ Zoom did NOT change.")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
