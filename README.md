# Double Click in Selenium

This project demonstrates how to perform a **double-click action in Selenium** using three different languages:

- 🐍 **Python**
- ☕ **Java**
- 🟨 **JavaScript (Node.js)**

Each implementation interacts with the same test page hosted on **LambdaTest** and simulates a real-world double-click on a blog title.

## 📁 Folder Structure

---

double-click-in-selenium/

│

├── Python/

│   ├── main.py

│   └── venv/                  # Python virtual environment

│

├── Java/

│   ├── main.java

│   └── models/                # (Optional) supporting classes or utilities

│

├── JavaScript/

│   ├── index.js

│   └── node_modules/          # Installed NPM dependencies

│

└── README.md

## 🧩 1. Setup & Run — Python Version

```bash
cd Python
python -m venv venv
venv\Scripts\activate   # (Windows)
# or source venv/bin/activate (macOS/Linux)

pip install selenium
python main.py

```

### ✅ Expected Output

```
Double-click action performed successfully on the blog title!

```

---

## 🟨 2. Setup & Run — JavaScript (Node.js) Version

### 📦 Requirements

- Node.js 18+
- Google Chrome
- Matching ChromeDriver

### ▶️ Steps

```bash
cd JavaScript
npm init -y
npm install selenium-webdriver chromedriver
node index.js

```

### ✅ Expected Output

```
Double-click action performed successfully on the blog title!

```

---

## ☕ 3. Setup & Run — Java Version

### 📦 Requirements

- Java JDK 17 or higher
- [Selenium Java Client](https://www.selenium.dev/downloads/)
- ChromeDriver

### ▶️ Steps

1. Open a terminal in the `Java` folder
2. Compile the Java file:
    
    ```bash
    javac -cp "selenium-server-4.x.x.jar;." main.java
    
    ```
    
3. Run the program:
    
    ```bash
    java -cp "selenium-server-4.x.x.jar;." main
    
    ```
    

### ✅ Expected Output

```
Double-click action performed successfully on the blog title!

```

---

## 🌐 Tested Site

All examples perform a double-click on this demo blog title:

> LambdaTest Playground – Blog Article
> 

---

## 🧠 Notes

- Each implementation opens Chrome, scrolls to the article title, and performs a realistic double-click using Selenium’s **ActionChains / Actions / Actions()** API.
- Ensure the correct ChromeDriver is installed and matches your Chrome browser version.
- Each folder maintains its own environment (`venv` for Python, `node_modules` for JavaScript) to keep dependencies isolated.

---

## 🧰 Optional Improvements

- Add logging or screenshot capture after double-click.
- Run tests in headless mode (`-headless`) for CI/CD pipelines.
- Integrate with LambdaTest or other remote WebDriver platforms.

---

## 👨‍💻 Author

**Alex Anie**

💡 Technical Writer & Web Automation Enthusiast

📚 Demonstrating Selenium best practices across languages

---

##