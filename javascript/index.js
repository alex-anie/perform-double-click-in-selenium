// index.js
const { Builder, By, until, Key, Actions } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async function doubleClickTest() {
  // --- Setup Chrome WebDriver ---
  const options = new chrome.Options();
  options.addArguments('--start-maximized');

  let driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

  try {
    // Step 1: Visit the LambdaTest demo blog page
    await driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37");

    // Step 2: Wait for the article title element to be visible
    const locator = By.css("#entry_210903 > h1");
    await driver.wait(until.elementLocated(locator), 10000);
    const articleTitle = await driver.findElement(locator);

    // Step 3: Scroll into view for clarity
    await driver.executeScript("arguments[0].scrollIntoView(true);", articleTitle);
    await driver.sleep(1000);

    // Step 4: Perform a realistic double-click action
    const actions = driver.actions({ bridge: true });
    await actions.doubleClick(articleTitle).perform();

    console.log("Double-click action performed successfully on the blog title!");

    // Step 5: Pause briefly to observe action
    await driver.sleep(2000);

  } catch (err) {
    console.error("Error during test:", err);
  } finally {
    await driver.quit();
  }
})();
