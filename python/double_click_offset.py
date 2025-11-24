from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re

def get_location_from_url(url):
    """
    Extract coordinates from the URL.
    OpenStreetMap encodes the location in the URL as #map=zoom/lat/lon
    """
    match = re.search(r"#map=\d+/([-.\d]+)/([-.\d]+)", url)
    if match:
        lat, lon = match.groups()
        return f"Lat: {lat}, Lon: {lon}"
    return "Unknown location"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Visit OpenStreetMap
    driver.get("https://www.openstreetmap.org/")
    wait = WebDriverWait(driver, 15)

    # Locate search field and type 'Nigeria'
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content input#query")))
    search_box.clear()
    search_box.send_keys("USA")
    search_box.send_keys(Keys.ENTER)
    print("Searched for USA...")

    # Wait for map to load
    time.sleep(5)

    # Initial location info
    initial_location = get_location_from_url(driver.current_url)
    print("Initial Location:", initial_location)

    # Double-click on map using offset (simulate zoom on another area)
    map_area = wait.until(EC.presence_of_element_located((By.ID, "map")))
    actions = ActionChains(driver)
    
    # Offset coordinates inside the map; adjust values as needed
    actions.move_to_element_with_offset(map_area, 150, 100).double_click().perform()
    print("Double-click with offset performed successfully.")

    # Wait for zoom animation / map update
    time.sleep(3)

    # Get new location from URL
    new_location = get_location_from_url(driver.current_url)
    print("New Location after double-click zoom:", new_location)

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(2)
    driver.quit()
