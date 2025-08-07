from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import random
import threading

app = Flask(__name__)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform"
TOTAL_RESPONSES = 80

# Random options
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

def fill_form():
    try:
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service("/usr/bin/chromedriver"),
            options=chrome_options
        )

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

        selected_platforms = random.sample(platforms, random.randint(2, 4))
        for platform in selected_platforms:
            driver.find_element(By.XPATH, f'//div[@data-value="{platform}"]').click(); time.sleep(0.2)

        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(reactions)}"]').click(); time.sleep(0.5)
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(agree_options)}"]').click(); time.sleep(0.5)

        driver.find_element(By.XPATH, '//span[text()="Submit"]').click()
        print(f"✅ Submitted at {datetime.now()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

def schedule_submissions():
    def run():
        for i in range(TOTAL_RESPONSES):
            delay = random.randint(60, 90) * 60  # 60–90 minutes
            threading.Timer(delay * i, fill_form).start()
    threading.Thread(target=run).start()

@app.route("/")
def home():
    return "✅ Bot is live"

@app.route("/submit")
def submit_once():
    try:
        fill_form()
        return "✅ Submitted 1 form"
    except Exception as e:
        return f"❌ Error: {e}"

@app.route("/start")
def start_auto():
    try:
        schedule_submissions()
        return "🕒 Scheduled 80 responses over 24 hours"
    except Exception as e:
        return f"❌ Scheduler failed: {e}"

@app.errorhandler(Exception)
def handle_error(e):
    return f"❌ Internal Server Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
