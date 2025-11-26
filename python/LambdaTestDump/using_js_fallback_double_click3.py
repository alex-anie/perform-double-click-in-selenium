# file: double_click_fallback.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def js_double_click(driver, element):
    """Fallback double-click using JavaScript when ActionsChains fails."""
    script = """
        var target = arguments[0];
        var event = new MouseEvent('dblclick', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        target.dispatchEvent(event);
    """
    driver.execute_script(script, element)


def test_double_click_with_fallback():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # TRUE DOUBLE-CLICK TEST WEBSITE
    driver.get("https://testpages.herokuapp.com/styled/events/events-doubleclick.html")
    time.sleep(2)

    target = driver.find_element(By.ID, "dblclick")
    actions = ActionChains(driver)

    try:
        print("Trying Selenium native double-click...")
        actions.double_click(target).perform()
        time.sleep(1)

        message = driver.find_element(By.ID, "buttonstatus").text
        print("Result:", message)

        # If the message does not confirm a double click, we consider it failed
        if "Double Click" not in message:
            raise Exception("Native double-click did not register correctly.")

    except Exception as e:
        print("Native double-click failed → switching to JavaScript fallback")
        js_double_click(driver, target)
        time.sleep(1)

        message = driver.find_element(By.ID, "buttonstatus").text
        print("Fallback Result:", message)

    driver.quit()


if __name__ == "__main__":
    test_double_click_with_fallback()
