from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def js_double_click(driver, element):
    """
    JavaScript fallback for double-click using a MouseEvent.
    """
    script = """
        var target = arguments[0];
        var evt = new MouseEvent('dblclick', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        target.dispatchEvent(evt);
    """
    driver.execute_script(script, element)
    print("[ACTION] JavaScript double-click fallback executed.")


def safe_double_click(driver, element):
    """
    First try Selenium's native double-click.
    If it fails, use JavaScript fallback.
    """
    try:
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        print("[ACTION] Selenium double-click succeeded.")
    except Exception as e:
        print("[WARNING] Selenium double-click failed → using JS fallback")
        print("Reason:", e)
        js_double_click(driver, element)


def test_js_fallback_double_click():
    # Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Navigate to copyright-free testing page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(2)

        print("[INFO] Page loaded:", driver.title)

        # Locate a clickable button
        button = driver.find_element(By.ID, "add_btn")
        print("[INFO] Found button with ID 'add_btn'")

        # Attempt double-click using safe approach
        safe_double_click(driver, button)

        time.sleep(2)

        # Print page status for confirmation
        print("[RESULT] Current URL:", driver.current_url)

    except Exception as e:
        print("[ERROR] Test encountered an exception:", e)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_js_fallback_double_click()
