from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ===========================================
# Double-Click on Dynamically Loaded Element Inside Nested Iframes
# ===========================================

driver = webdriver.Chrome()

try:
    # Visit a website containing nested iframes (W3Schools demo page)
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
    wait = WebDriverWait(driver, 15)

    # ----- STEP 1: Switch to outer iframe -----
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

    # The demo loads a button with ondblclick event (dynamic rendering inside iframe)
    target_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Double-click me']"))
    )

    # ----- STEP 2: Double-click the element -----
    actions = ActionChains(driver)
    actions.double_click(target_element).perform()

    time.sleep(2)

    # ----- STEP 3: Verify change after double-click -----
    result = wait.until(
        EC.presence_of_element_located((By.ID, "demo"))
    )

    print("✔ Double-click executed successfully!")
    print("Text After Double-Click:", result.text)

except Exception as e:
    print("❌ An error occurred:", str(e))

finally:
    time.sleep(3)
    driver.quit()
