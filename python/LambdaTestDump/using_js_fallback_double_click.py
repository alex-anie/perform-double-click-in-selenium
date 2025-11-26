from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def double_click_with_js_fallback(driver, element):
    """
        Attempts a standard Selenium double-click.
        If it fails (due to overlay, animation, or browser bug),
        fall back to JavaScript-based double-click dispatch.
    """
    try:
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        print("[ACTION] Standard Selenium double-click succeeded.")
    except Exception as e:
        print("[WARNING] Selenium double-click failed. Falling back to JavaScript...")
        print("Error:", e)

        # JavaScript fallback using MouseEvent dblclick simulation
        js_script = """
            var target = arguments[0];
            var evt = new MouseEvent('dblclick', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            target.dispatchEvent(evt);
        """
        driver.execute_script(js_script, element)
        print("[ACTION] JavaScript double-click executed.")


def test_js_fallback_double_click():
    # Start Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Navigate to LambdaTest demo store
        driver.get("https://ecommerce-playground.lambdatest.io/")
        time.sleep(3)

        # Locate a product tile (e.g., the first product card on the homepage)
        product_card = driver.find_element(By.CSS_SELECTOR, ".product-layout .product-thumb")
        print("[INFO] Product card located.")

        # Try to double-click using standard Selenium → fallback to JS if needed
        double_click_with_js_fallback(driver, product_card)

        time.sleep(2)

        # Confirm navigation or action occurred (e.g., product detail page loaded)
        print("[RESULT] Current page title:", driver.title)

    except Exception as e:
        print("[ERROR] Test failed:", e)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_js_fallback_double_click()
