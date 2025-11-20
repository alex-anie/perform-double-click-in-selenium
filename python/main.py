from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

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
    "build": "Selenium Double Click Actions",
    "project": "Running Python Scripts",
    "name": "Perform a realistic double-click action",
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
    # Step 1: Visit the demo blog page
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37")

    # Step 2: Wait for the article title
    wait = WebDriverWait(driver, 10)
    article_title = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#entry_210903 > h1")
        )
    )

    # Step 3: Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", article_title)
    time.sleep(1)

    # Step 4: Double-click the title
    actions = ActionChains(driver)
    actions.double_click(article_title).perform()

    print("Double-click action performed successfully on LambdaTest!")

    # Step 5: Allow time for visual verification
    time.sleep(2)

    # Mark test as passed on LambdaTest (if desired)
    driver.execute_script("lambda-status=passed")

finally:
    driver.quit()
