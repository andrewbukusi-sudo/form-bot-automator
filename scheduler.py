import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def submit_form():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Tell Selenium where the correct ChromeDriver is
    service = Service("/usr/local/bin/chromedriver")  # Use downloaded one that matches Chromium 139

    # Launch browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open your form
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")

        time.sleep(3)

        # Select Age
        age_options = ["18–24", "25–34", "35–44", "45 and above"]
        age = random.choice(age_options)
        age_xpath = f'//div[@data-value="{age}"]'
        driver.find_element(By.XPATH, age_xpath).click()

        # Select Gender
        gender_options = ["Male", "Female", "Prefer not to say"]
        gender = random.choice(gender_options)
        gender_xpath = f'//div[@data-value="{gender}"]'
        driver.find_element(By.XPATH, gender_xpath).click()

        # Seen wildlife photos
        seen = random.choice(["Yes", "No"])
        seen_xpath = f'//div[@data-value="{seen}"]'
        driver.find_element(By.XPATH, seen_xpath).click()

        # Frequency (only if "Yes")
        if seen == "Yes":
            freq = random.choice(["Very often", "Often", "Sometimes", "Rarely", "Never"])
            freq_xpath = f'//div[@data-value="{freq}"]'
            driver.find_element(By.XPATH, freq_xpath).click()

        # Awareness from photojournalism
        awareness = random.choice(["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"])
        awareness_xpath = f'//div[@data-value="{awareness}"]'
        driver.find_element(By.XPATH, awareness_xpath).click()

        # Effectiveness scale (1–5)
        effectiveness = str(random.randint(1, 5))
        effectiveness_xpath = f'//div[@data-value="{effectiveness}"]'
        driver.find_element(By.XPATH, effectiveness_xpath).click()

        # Platforms (multi-choice)
        platform_options = [
            "Newspapers", "Magazines", "Social media", 
            "Online news websites", "TV broadcasts", "Photography exhibitions"
        ]
        selected_platforms = random.sample(platform_options, random.randint(1, 3))
        for platform in selected_platforms:
            xpath = f'//div[@data-value="{platform}"]'
            driver.find_element(By.XPATH, xpath).click()

        # Most impactful
        impactful = random.choice(platform_options)
        impactful_xpath = f'//div[@data-value="{impactful}"]'
        driver.find_element(By.XPATH, impactful_xpath).click()

        # Reaction
        reaction = random.choice([
            "Feel concerned but take no action",
            "Feel motivated to learn more",
            "Feel motivated to take action (e.g., donate, volunteer)",
            "No particular reaction"
        ])
        reaction_xpath = f'//div[@data-value="{reaction}"]'
        driver.find_element(By.XPATH, reaction_xpath).click()

        # Support for conservation
        support = random.choice(["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"])
        support_xpath = f'//div[@data-value="{support}"]'
        driver.find_element(By.XPATH, support_xpath).click()

        # Submit
        submit_btn = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
        submit_btn.click()

        print("✅ Form submitted.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        driver.quit()
