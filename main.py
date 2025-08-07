from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, random
from datetime import datetime

app = Flask(__name__)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform"

# Data pools
age_options = ["Below 18", "18–24", "25–34"]
gender_options = ["Male", "Female", "Prefer not to say"]
education_levels = ["Secondary", "College/University", "Postgraduate"]
frequency_options = ["Very often", "Often", "Sometimes", "Rarely", "Never"]
agree_options = ["Strongly agree", "Agree", "Neutral", "Disagree", "Strongly disagree"]
rating_scale = ["1", "2", "3", "4", "5"]
platforms = ["Newspapers", "Magazines", "Social media", "Online news websites", "TV broadcasts", "Photography exhibitions"]
reactions = [
    "Feel concerned but take no action",
    "Feel motivated to learn more",
    "Feel motivated to take action (e.g., donate, volunteer)",
    "No particular reaction"
]

def submit_response():
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(FORM_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(age_options)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(gender_options)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(education_levels)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("Student"); time.sleep(0.5)
        driver.find_element(By.XPATH, '//div[@data-value="Yes"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(frequency_options)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(agree_options)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//span[text()="{random.choice(rating_scale)}"]').click(); time.sleep(0.5)
        sel = random.sample(platforms, random.randint(2, 4))
        for p in sel:
            driver.find_element(By.XPATH, f'//div[@data-value="{p}"]').click(); time.sleep(0.2)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(platforms)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(reactions)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(agree_options)}"]').click(); time.sleep(0.5)

        driver.find_element(By.XPATH, '//span[text()="Submit"]').click()
        print(f"[{datetime.now()}] ✅ Submitted successfully")

    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error submitting: {e}")
    finally:
        driver.quit()

@app.route("/")
def home():
    return "Form bot is running!"

@app.route("/submit")
def manual_submit():
    submit_response()
    return "Submitted one response!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)