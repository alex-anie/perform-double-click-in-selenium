from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ===== Local Chrome WebDriver =====
driver = webdriver.Chrome()

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

    # Select all text in the input field (CTRL + A)
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

finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ===== Local Chrome WebDriver =====
driver = webdriver.Chrome()

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

    # Select all text in the input field (CTRL + A)
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

finally:
    driver.quit()
