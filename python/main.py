from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ===== Local Chrome WebDriver =====
driver = webdriver.Chrome()

try:
    # Step 1: Visit the demo blog page
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37")

    # Step 2: Wait for the article title to load
    wait = WebDriverWait(driver, 10)
    article_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#entry_210903 > h1"))
    )

    # Step 3: Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", article_title)
    time.sleep(1)

    # Step 4: Perform a double-click on the title
    actions = ActionChains(driver)
    actions.double_click(article_title).perform()

    print("Double-click action performed successfully!")

    # Step 5: Pause for verification
    time.sleep(2)

finally:
    driver.quit()
