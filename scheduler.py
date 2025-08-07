import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Setup Chrome driver options
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless=new")  # Keep headless in production

    service = Service("/usr/local/bin/chromedriver")
    return webdriver.Chrome(service=service, options=chrome_options)

# Helper to simulate typing into a contenteditable div
def type_into_div(driver, label_text, input_text):
    time.sleep(1)
    labels = driver.find_elements(By.XPATH, f'//div[@aria-label="{label_text}"]')
    if not labels:
        print(f"❌ Label '{label_text}' not found.")
        return

    target = labels[0]
    actions = ActionChains(driver)
    actions.move_to_element(target).click().pause(0.5).send_keys(input_text).perform()
    print(f"✅ Typed '{input_text}' into '{label_text}'")

# Submit one Google Form response
def submit_form():
    try:
        driver = get_driver()
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")
        time.sleep(3)

        # Age
        age_choices = ["18–24", "25–34", "35–44", "45 and above"]
        age = random.choice(age_choices)
        type_into_div(driver, "Age", age)

        # Gender
        gender_choices = ["Male", "Female", "Prefer not to say"]
        gender = random.choice(gender_choices)
        type_into_div(driver, "Gender", gender)

        # Other multiple-choice & scale questions
        def click_by_label(text):
            try:
                el = driver.find_element(By.XPATH, f'//span[text()="{text}"]')
                el.click()
                print(f"✅ Clicked '{text}'")
            except:
                print(f"❌ Could not click '{text}'")

        click_by_label(random.choice(["Yes", "No"]))
        time.sleep(0.5)

        click_by_label(random.choice(["Very often", "Often", "Sometimes", "Rarely", "Never"]))
        time.sleep(0.5)

        click_by_label(random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ]))
        time.sleep(0.5)

        click_by_label(random.choice(["1", "2", "3", "4", "5"]))
        time.sleep(0.5)

        platforms = [
            "Newspapers", "Magazines", "Social media",
            "Online news websites", "TV broadcasts", "Photography exhibitions"
        ]
        for _ in range(random.randint(1, 3)):
            click_by_label(random.choice(platforms))
            time.sleep(0.5)

        click_by_label(random.choice(platforms))  # Most impactful
        time.sleep(0.5)

        click_by_label(random.choice([
            "Feel concerned but take no action",
            "Feel motivated to learn more",
            "Feel motivated to take action (e.g., donate, volunteer)",
            "No particular reaction"
        ]))
        time.sleep(0.5)

        click_by_label(random.choice([
            "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"
        ]))
        time.sleep(0.5)

        # Submit form
        submit_btn = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
        submit_btn.click()
        print("✅ Form submitted successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
