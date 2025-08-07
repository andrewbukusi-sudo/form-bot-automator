import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def submit_form():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")

    try:
        # Age
        age_option = random.choice(["18–24", "25–34", "35–44", "45 and above"])
        driver.find_element(By.XPATH, f'//div[@data-value="{age_option}"]').click()
        time.sleep(0.5)

        # Gender
        gender_option = random.choice(["Male", "Female", "Prefer not to say"])
        driver.find_element(By.XPATH, f'//div[@data-value="{gender_option}"]').click()
        time.sleep(0.5)

        # Seen wildlife photos
        seen_option = random.choice(["Yes", "No"])
        driver.find_element(By.XPATH, f'//div[@data-value="{seen_option}"]').click()
        time.sleep(0.5)

        # Frequency (if Yes was selected)
        if seen_option == "Yes":
            freq_option = random.choice(["Very often", "Often", "Sometimes", "Rarely", "Never"])
            driver.find_element(By.XPATH, f'//div[@data-value="{freq_option}"]').click()
            time.sleep(0.5)

        # Agreement with awareness impact
        awareness_agreement = random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{awareness_agreement}"]').click()
        time.sleep(0.5)

        # Effectiveness scale (1–5)
        effectiveness = str(random.randint(1, 5))
        driver.find_element(By.XPATH, f'//div[@data-value="{effectiveness}"]').click()
        time.sleep(0.5)

        # Platforms for photojournalism (checkboxes - random multiple)
        platforms = [
            "Newspapers", "Magazines", "Social media",
            "Online news websites", "TV broadcasts", "Photography exhibitions"
        ]
        selected_platforms = random.sample(platforms, k=random.randint(1, 3))
        for platform in selected_platforms:
            driver.find_element(By.XPATH, f'//div[@data-value="{platform}"]').click()
            time.sleep(0.3)

        # Most impactful platform (radio)
        impactful_platform = random.choice(platforms)
        driver.find_element(By.XPATH, f'//div[@data-value="{impactful_platform}"]').click()
        time.sleep(0.5)

        # Reaction to wildlife photographs
        reaction = random.choice([
            "Feel concerned but take no action",
            "Feel motivated to learn more",
            "Feel motivated to take action (e.g., donate, volunteer)",
            "No particular reaction"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{reaction}"]').click()
        time.sleep(0.5)

        # Agreement with support for conservation
        support_agreement = random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ])
        driver.find_element(By.XPATH, f'//div[@data-value="{support_agreement}"]').click()
        time.sleep(0.5)

        # Submit
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
        submit_button.click()

        print("✅ Submitted successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    submit_form()
