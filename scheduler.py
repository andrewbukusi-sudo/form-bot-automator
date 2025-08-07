from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def submit_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode on Render
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Go to your actual Google Form URL
        driver.get("https://docs.google.com/forms/d/e/your-form-id/viewform")
        time.sleep(3)

        # ---- 1. Age ----
        age_options = ["18–24", "25–34", "35–44", "45 and above"]
        age_choice = random.choice(age_options)
        age_input = driver.find_element(By.XPATH, f'//input[@value="{age_choice}"]')
        age_input.click()
        time.sleep(1)

        # ---- 2. Gender ----
        gender_options = ["Male", "Female", "Prefer not to say"]
        gender_choice = random.choice(gender_options)
        gender_input = driver.find_element(By.XPATH, f'//input[@value="{gender_choice}"]')
        gender_input.click()
        time.sleep(1)

        # ---- 3. Seen wildlife photos? ----
        seen_options = ["Yes", "No"]
        seen_choice = random.choice(seen_options)
        seen_input = driver.find_element(By.XPATH, f'//input[@value="{seen_choice}"]')
        seen_input.click()
        time.sleep(1)

        # ---- 4. Frequency (only if "Yes") ----
        if seen_choice == "Yes":
            freq_options = ["Very often", "Often", "Sometimes", "Rarely", "Never"]
            freq_choice = random.choice(freq_options)
            freq_input = driver.find_element(By.XPATH, f'//input[@value="{freq_choice}"]')
            freq_input.click()
            time.sleep(1)

        # ---- 5. Agree with awareness ----
        agree_options = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
        agree_choice = random.choice(agree_options)
        agree_input = driver.find_element(By.XPATH, f'//input[@value="{agree_choice}"]')
        agree_input.click()
        time.sleep(1)

        # ---- 6. Effectiveness scale (1–5) ----
        effectiveness_options = ["Not effective", "1", "2", "3", "4", "5", "Highly effective"]
        effectiveness_choice = random.choice(effectiveness_options)
        effectiveness_input = driver.find_element(By.XPATH, f'//input[@value="{effectiveness_choice}"]')
        effectiveness_input.click()
        time.sleep(1)

        # ---- 7. Platforms used (multiple select) ----
        platform_options = [
            "Newspapers", "Magazines", "Social media",
            "Online news websites", "TV broadcasts", "Photography exhibitions"
        ]
        selected_platforms = random.sample(platform_options, k=random.randint(1, 3))
        for platform in selected_platforms:
            platform_input = driver.find_element(By.XPATH, f'//input[@value="{platform}"]')
            platform_input.click()
            time.sleep(0.5)

        # ---- 8. Most impactful platform ----
        impactful_choice = random.choice(platform_options)
        impactful_input = driver.find_element(By.XPATH, f'//input[@value="{impactful_choice}"]')
        impactful_input.click()
        time.sleep(1)

        # ---- 9. Reaction to photo ----
        reaction_options = [
            "Feel concerned but take no action",
            "Feel motivated to learn more",
            "Feel motivated to take action (e.g., donate, volunteer)",
            "No particular reaction"
        ]
        reaction_choice = random.choice(reaction_options)
        reaction_input = driver.find_element(By.XPATH, f'//input[@value="{reaction_choice}"]')
        reaction_input.click()
        time.sleep(1)

        # ---- 10. Agree with support due to photographs ----
        support_agree_choice = random.choice(agree_options)
        support_input = driver.find_element(By.XPATH, f'//input[@value="{support_agree_choice}"]')
        support_input.click()
        time.sleep(1)

        # ---- Submit the form ----
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
        submit_button.click()
        time.sleep(2)

        print("✅ Submitted form successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()
