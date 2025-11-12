// Main.java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Main {
    public static void main(String[] args) {
        // --- Setup Chrome WebDriver ---
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        try {
            // Step 1: Visit the LambdaTest demo blog page
            driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37");

            // Step 2: Wait for the article title element to be visible
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            WebElement articleTitle = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#entry_210903 > h1"))
            );

            // Step 3: Scroll into view for clarity
            ((org.openqa.selenium.JavascriptExecutor) driver)
                .executeScript("arguments[0].scrollIntoView(true);", articleTitle);
            Thread.sleep(1000);

            // Step 4: Perform a realistic double-click action
            Actions actions = new Actions(driver);
            actions.doubleClick(articleTitle).perform();

            System.out.println("✅ Double-click action performed successfully on the blog title!");

            // Step 5: Pause briefly to observe action
            Thread.sleep(2000);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
}
