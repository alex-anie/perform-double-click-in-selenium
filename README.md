# **Double Click in Selenium (Python Project)**

This project demonstrates how to perform a **realistic double-click action using Selenium in Python** on a LambdaTest demo blog page.

You will run the test using:

✔ **Local ChromeDriver**

✔ **LambdaTest Cloud Grid (Remote WebDriver)**

The entry script for this project is:

```
main.py
```

---

# 📁 **Folder Structure**

```
double-click-in-selenium/
│
├── Python/
│   ├── main.py
│   ├── requirements.txt
│   └── venv/                 # Python virtual environment (created after setup)
│
└── README.md
```

---

# 🧩 **1. Setup & Run — Python Version**

Follow these steps to set up the project locally:

### **Step 1 — Navigate to the Python folder**

```bash
cd Python
```

---

### **Step 2 — Create & Activate Virtual Environment**

### **Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### **macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **Step 3 — Install Required Dependencies**

Your `requirements.txt` includes all necessary packages:

```
attrs==25.4.0
certifi==2025.11.12
cffi==2.0.0
h11==0.16.0
idna==3.11
outcome==1.3.0.post0
pycparser==2.23
PySocks==1.7.1
python-dotenv==1.2.1
selenium==4.38.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.32.0
trio-websocket==0.12.2
typing_extensions==4.15.0
urllib3==2.5.0
websocket-client==1.9.0
wsproto==1.3.1
```

Install them:

```bash
pip install -r requirements.txt
```

---

# 🚀 **2. Run Test Locally (ChromeDriver)**

Simply run:

```bash
python main.py
```

You should see:

```
Double-click action performed successfully on the blog title!
```

---

# ☁️ **3. Run the Test on LambdaTest (Remote WebDriver)**

To run your Selenium script on the LambdaTest cloud grid, follow the steps below.

---

## **Step 1 — Get Your Credentials**

Log in to your LambdaTest account and fetch:

- **Username**
- **Access Key**

---

## **Step 2 — Set Environment Variables**

Your script uses:

```
LT_USERNAME
LT_ACCESS_KEY
```

### **Linux/macOS**

```bash
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR_ACCESS_KEY"
```

### **Windows (CMD)**

```bash
set LT_USERNAME="YOUR_USERNAME"
set LT_ACCESS_KEY="YOUR_ACCESS_KEY"
```

### **Windows (PowerShell)**

```powershell
$env:LT_USERNAME="YOUR_USERNAME"
$env:LT_ACCESS_KEY="YOUR_ACCESS_KEY"
```

---

## **Step 3 — Run the Test**

Once environment variables are set, simply execute:

```bash
python main.py
```

The script will:

1. Connect to the LambdaTest Selenium Grid
2. Launch Chrome on Windows 11
3. Navigate to the blog article
4. Scroll to the heading
5. Perform a double-click interaction
6. Record test video, logs & execution results on LambdaTest

You can view test insights in your dashboard:

**LambdaTest Dashboard → Automation → Test Logs**

---

# 🌐 **Test Page Used**

All interactions occur on the LambdaTest Playground blog:

```
https://ecommerce-playground.lambdatest.io/index.php?route=extension/maza/blog/article&article_id=37
```

---

# 🧠 **Notes**

- Ensure Chrome is installed if running locally.
- Chromedriver is automatically managed by Selenium 4 on most setups.
- Use virtual environments to avoid dependency conflicts.
- Switching between **local WebDriver** and **LambdaTest Remote WebDriver** is handled inside `main.py`.

---

# 📌 **Optional Improvements**

- Add screenshot capturing after each double-click
- Run in headless mode for CI/CD
- Integrate with GitHub Actions for scheduled cross-browser cloud testing
- Add assertion checks for validation

---

# 👨‍💻 **Author**

**Alex Anie**

🧪 Automation Engineer & Technical Writer

📚 Exploring Selenium best practices & cloud-based testing