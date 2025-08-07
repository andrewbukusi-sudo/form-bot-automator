from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
from datetime import datetime

app = Flask(__name__)

CHROME_DRIVER_PATH = "/usr/bin/chromedriver"  # default path on Render
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform"

# === FIELD OPTIONS ===
age_options = ["Below 18", "18–24", "25–34"]
gender_options = ["Male", "Female"]
yes_no_options = ["Yes", "No"]
rating_scale = ["1", "2", "3", "4", "5"]
platforms = ["Social media", "TV broadcasts", "Magazines", "Online news websites", "Photography exhibitions"]

def submit_response():
    options = Options()
    options.add_argument('--headless')  # Comment this line to debug with visible browser
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
        driver.get(FORM_URL)
        time.sleep(3)

        # Q1: Age
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(age_options)}"]').click()
        time.sleep(0.5)

        # Q2: Gender
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(gender_options)}"]').click()
        time.sleep(0.5)

        # Q3: Have you seen photographs (Yes/No)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(yes_no_options)}"]').click()
        time.sleep(0.5)

        # Q4: Rate effectiveness (1–5)
        driver.find_element(By.XPATH, f'//span[text()="{random.choice(rating_scale)}"]').click()
        time.sleep(0.5)

        # Q5: Platform(s)
        selected_platforms = random.sample(platforms, k=random.randint(1, 3))
        for p in selected_platforms:
            try:
                driver.find_element(By.XPATH, f'//div[@data-value="{p}"]').click()
                time.sleep(0.2)
            except:
                continue  # skip if platform not found

        # Submit the form
        driver.find_element(By.XPATH, '//span[text()="Submit"]').click()
        print(f"[{datetime.now()}] ✅ Submitted successfully")

    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error: {e}")
    finally:
        driver.quit()

@app.route("/")
def home():
    return "Form Bot is running!"

@app.route("/submit")
def manual_submit():
    submit_response()
    return "Submitted 1 form"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
