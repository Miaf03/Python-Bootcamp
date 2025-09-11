import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Load variables from .env file
load_dotenv()
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

# ---------------- Selenium Setup ----------------
chrome_options = webdriver.ChromeOptions()
# Keep the browser open even if the script finishes
chrome_options.add_experimental_option("detach", True)
# Create a persistent Chrome profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)

# Open the gym page
driver.get(GYM_URL)

# ---------------- Retry Function ----------------
def retry(func, retries=7, description=None):
    """Try to run a function several times in case of TimeoutException"""
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

# ---------------- Automatic Login ----------------
def login():
    """Perform login using credentials from .env"""
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
    print("✅ Login successful")

# ---------------- Book Class Function ----------------
def book_class(booking_button):
    """Book or join waitlist depending on the button"""
    booking_button.click()
    wait.until(lambda d: booking_button.text in ["Booked", "Waitlisted"])

# Run login with retries
retry(login, description="login")

# ---------------- Find and Book Specific Classes ----------------
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_count = 0
waitlist_count = 0
already_booked_count = 0

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Only Tuesday and Thursday
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        # Only 6:00 PM
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title} at {time_text}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
            elif button.text == "Book Class":
                retry(lambda: book_class(button), description=f"Booking {class_info}")
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description=f"Waitlisting {class_info}")
                print(f"✓ Joined waitlist: {class_info}")
                waitlist_count += 1
            time.sleep(0.5)

# ---------------- Verification in My Bookings ----------------
def get_my_bookings():
    my_bookings_link = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()
    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not cards:
        raise TimeoutException("No bookings found")
    return cards

all_cards = retry(get_my_bookings, description="Get my bookings")

verified_count = 0
total_booked = already_booked_count + booked_count + waitlist_count

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        continue

print(f"\n--- Total Tue/Thu 6 PM classes: {total_booked} ---")
print(f"--- Verified bookings: {verified_count} ---")

if total_booked == verified_count:
    print("SUCCESS: All bookings verified")
else:
    print(f"MISMATCH: Missing {total_booked - verified_count} bookings")