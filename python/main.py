from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup Chrome WebDriver ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Visit the LambdaTest demo blog page
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37")

    # Step 2: Wait for the article title element to be visible
    wait = WebDriverWait(driver, 10)
    article_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#entry_210903 > h1")))

    # Step 3: Scroll into view for clarity
    driver.execute_script("arguments[0].scrollIntoView(true);", article_title)
    time.sleep(1)

    # Step 4: Perform a realistic double-click action
    actions = ActionChains(driver)
    actions.double_click(article_title).perform()

    print("Double-click action performed successfully on the blog title!")

    # Step 5: Pause briefly to observe action
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
