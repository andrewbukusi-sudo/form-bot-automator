import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def submit_form():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(2)

        # AGE
        age_options = [
            "18–24", "25–34", "35–44", "45 and above"
        ]
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(age_options)}"]').click()

        # GENDER
        gender_options = ["Male", "Female", "Prefer not to say"]
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(gender_options)}"]').click()

        # Seen wildlife photo
        driver.find_element(By.XPATH, f'//div[@data-value="{random.choice(["Yes", "No"])}"]').click()

        # Frequency
        freq = random.choice(["Very often", "Often", "Sometimes", "Rarely", "Never"])
        driver.find_element(By.XPATH, f'//div[@data-value="{freq}"]').click()

        # Awareness from photojournalism
        awareness = random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{awareness}"]').click()

        # Effectiveness scale 1–5
        driver.find_element(By.XPATH, f'//div[@data-value="{str(random.randint(1,5))}"]').click()

        # Platforms (multiple choice)
        platforms = [
            "Newspapers", "Magazines", "Social media", 
            "Online news websites", "TV broadcasts", "Photography exhibitions"
        ]
        random.shuffle(platforms)
        for platform in platforms[:random.randint(1, 4)]:
            driver.find_element(By.XPATH, f'//div[@data-value="{platform}"]').click()

        # Most impactful platform (single)
        impactful = random.choice(platforms)
        driver.find_element(By.XPATH, f'//div[@data-value="{impactful}"]').click()

        # Reaction
        reaction = random.choice([
            "Feel concerned but take no action",
            "Feel motivated to learn more",
            "Feel motivated to take action (e.g., donate, volunteer)",
            "No particular reaction"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{reaction}"]').click()

        # Support conservation from photos
        support = random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{support}"]').click()

        # Submit
        submit_btn = driver.find_element(By.XPATH, '//span[contains(text(),"Submit")]/ancestor::div[@role="button"]')
        submit_btn.click()

        print("✅ Submitted form successfully")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()
