from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_combined_interactions():
    # Start browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Go to a free demo website
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    # Hover over the double-click button
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.move_to_element(double_click_btn).perform()
    time.sleep(1)

    # Now double-click it
    actions.double_click(double_click_btn).perform()
    print("Double-click message:", driver.find_element(By.ID, "doubleClickMessage").text)

    # Navigate to draggable test
    driver.get("https://demoqa.com/droppable")
    time.sleep(1)

    drag_box = driver.find_element(By.ID, "draggable")
    drop_box = driver.find_element(By.ID, "droppable")

    # Drag → Drop
    actions.drag_and_drop(drag_box, drop_box).perform()
    time.sleep(1)

    print("Drop box text after drop:", drop_box.text)

    # For demonstration, double-click the drop-box element
    actions.double_click(drop_box).perform()
    print("Double-click performed on drop box!")

    # Cleanup
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    test_combined_interactions()
