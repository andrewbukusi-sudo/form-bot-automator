from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def submit_form():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(2)

    try:
        # Select Age
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="18–24"]]').click()

        # Select Gender
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Male"]]').click()

        # Seen conservation photos?
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Yes"]]').click()

        # Frequency of seeing such photos
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Often"]]').click()

        # Agreement: awareness
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Agree"]]').click()

        # Effectiveness scale: 5
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="5"]]').click()

        # Platforms seen on
        driver.find_element(By.XPATH, '//div[@role="checkbox" and .//div[text()="Social media"]]').click()

        # Most impactful platform
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Photography exhibitions"]]').click()

        # Reaction to photos
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Feel concerned but take no action"]]').click()

        # Agreement: support
        driver.find_element(By.XPATH, '//div[@role="radio" and .//div[text()="Strongly agree"]]').click()

        # Submit form
        driver.find_element(By.XPATH, '//span[text()="Submit"]').click()

        time.sleep(2)
        print("✅ Form submitted")

    except Exception as e:
        print(f"❌ Error: {e}")

    driver.quit()
