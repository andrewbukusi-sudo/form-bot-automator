import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def submit_form():
    driver = None
    try:
        # Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Use webdriver_manager to install and use the correct ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")
        time.sleep(3)

        # === Fill Age (editable div) ===
        age_options = ["18–24", "25–34", "35–44", "45 and above"]
        chosen_age = random.choice(age_options)
        age_div = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Age"]')[0]
        age_div.click()
        time.sleep(0.5)
        age_div.send_keys(chosen_age)
        age_div.send_keys(Keys.TAB)

        # === Fill Gender (editable div) ===
        gender_options = ["Male", "Female", "Prefer not to say"]
        chosen_gender = random.choice(gender_options)
        gender_div = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Gender"]')[0]
        gender_div.click()
        time.sleep(0.5)
        gender_div.send_keys(chosen_gender)
        gender_div.send_keys(Keys.TAB)

        time.sleep(1)

        # === Submit the form ===
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]')
        submit_button.click()

        print("✅ Form submitted.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if driver:
            driver.quit()
