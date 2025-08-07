import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def submit_form():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")

        time.sleep(3)

        # Random choices for each question
        age_options = ["18–24", "25–34", "35–44", "45 and above"]
        gender_options = ["Male", "Female", "Prefer not to say"]
        seen_photos = ["Yes", "No"]
        frequency = ["Very often", "Often", "Sometimes", "Rarely", "Never"]
        awareness = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
        effectiveness = ["1", "2", "3", "4", "5"]
        platforms = ["Newspapers", "Magazines", "Social media", "Online news websites", "TV broadcasts", "Photography exhibitions"]
        reactions = ["Feel concerned but take no action", "Feel motivated to learn more", "Feel motivated to take action (e.g., donate, volunteer)", "No particular reaction"]

        # Fill each field by visible text
        def click_option(value):
            xpath = f'//div[@role="listitem"]//span[contains(text(), "{value}")]'
            element = driver.find_element(By.XPATH, xpath)
            element.click()

        click_option(random.choice(age_options))
        click_option(random.choice(gender_options))
        click_option(random.choice(seen_photos))
        click_option(random.choice(frequency))
        click_option(random.choice(awareness))
        click_option(random.choice(effectiveness))
        click_option(random.choice(platforms))  # multiple choice platform
        click_option(random.choice(platforms))  # most impactful platform
        click_option(random.choice(reactions))
        click_option(random.choice(awareness))  # willingness to support

        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]/ancestor::div[@role="button"]')
        submit_button.click()

        print("✅ Form submitted.")
        driver.quit()

    except Exception as e:
        print(f"❌ Error: {e}")
