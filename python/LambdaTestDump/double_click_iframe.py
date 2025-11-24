from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# =======================================================
# Double-Click Interaction on Dynamically Loaded Element
# Using https://ecommerce-playground.lambdatest.io/
# =======================================================

driver = webdriver.Chrome()

try:
    # Step 1: Visit the main website
    driver.get("https://ecommerce-playground.lambdatest.io/")
    wait = WebDriverWait(driver, 15)

    # Step 2: Wait for page to load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # =======================================================
    # Handle dynamically loaded newsletter popup iframe
    # =======================================================

    try:
        # The popup loads after a delay, wrapped inside an iframe-like container
        popup_iframe = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[class*='ltkpopup']"))
        )

        driver.switch_to.frame(popup_iframe)

        close_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".close"))
        )
        close_btn.click()

        driver.switch_to.default_content()

        print("✔ Newsletter popup closed.")
    except:
        print("⚠ Popup did not appear — continuing.")

    time.sleep(1)

    # =======================================================
    # Step 3: Interact with a dynamically loaded search bar
    # Double-click inside the search field
    # =======================================================

    search_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='search']"))
    )

    search_box.send_keys("Laptop")
    time.sleep(1)

    # Perform double-click on the search field
    actions = ActionChains(driver)
    actions.double_click(search_box).perform()

    print("✔ Double-click executed on search field!")

    # Verify text selection by typing new text
    search_box.send_keys(" - Double Click Successful")
    time.sleep(2)

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    time.sleep(3)
    driver.quit()
