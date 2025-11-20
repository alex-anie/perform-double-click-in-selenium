from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

# Load .env credentials
load_dotenv()

username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

# LambdaTest Grid URL
grid_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

# ===== LambdaTest Capabilities =====
lt_options = {
    "username": username,
    "accessKey": access_key,
    "build": "Search and Double Click Action",
    "project": "Search, Double Click and verify test",
    "name": "Double click on an input field",
    "selenium_version": "4.0.0",
    "w3c": True,
    "visual": True,
    "video": True,
}

browser_caps = {
    "platformName": "Windows 11",
    "browserName": "Chrome",
    "browserVersion": "latest",
    "seCdp": True,
    "LT:Options": lt_options
}

# Convert caps properly for Selenium 4
options = Options()
for key, value in browser_caps.items():
    if key != "LT:Options":
        options.set_capability(key, value)

options.set_capability("LT:Options", lt_options)

# ===== Remote WebDriver for LambdaTest =====
driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

try:
    # Go to the main site
    driver.get("https://ecommerce-playground.lambdatest.io/")
    wait = WebDriverWait(driver, 10)

    # Locate the search bar and type "Apple iPhone"
    search_bar = wait.until(EC.presence_of_element_located((By.NAME, "search")))
    search_text = "Apple iPhone"
    search_bar.send_keys(search_text)
    time.sleep(1)  # Small pause to show typing

    # Double-click the text to select it
    actions = ActionChains(driver)
    actions.double_click(search_bar).perform()
    time.sleep(1)

    # selected  all text in the input field (CTRL + A)
    search_bar.send_keys(Keys.CONTROL, 'a')
    time.sleep(0.5)

    # Copy the selected text (CTRL + C)
    search_bar.send_keys(Keys.CONTROL, 'c')
    time.sleep(0.5)

    # Clear the input and paste copied text
    search_bar.clear()
    time.sleep(0.5)
    search_bar.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # Press Enter to search
    search_bar.send_keys(Keys.ENTER)

    # Verify search result (title should contain "Apple iPhone")
    wait.until(EC.title_contains("Apple iPhone"))

    page_title = driver.title

    if "Apple iPhone" in page_title:
        print("✔ Search verification successful!")
    else:
        print("❌ Search verification failed!")

    # Mark test as passed in LambdaTest
    driver.execute_script("lambda-status=passed")

finally:
    driver.quit()
