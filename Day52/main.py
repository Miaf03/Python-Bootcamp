import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(6)

        try:
            not_now = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not now') or contains(text(), 'Ahora no')]")
            not_now.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        try:
            followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        except NoSuchElementException:
            followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "seguidores")

        followers_link.click()
        time.sleep(5)

        self.modal = self.driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")

        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
            time.sleep(2)

    def follow(self, limit=10):
        time.sleep(3)
        all_buttons = self.modal.find_elements(By.CSS_SELECTOR, "button")

        count = 0
        for button in all_buttons:
            if count >= limit:
                break
            try:
                if button.text.lower() in ["follow", "seguir"]:
                    button.click()
                    count += 1
                    time.sleep(2)
            except ElementClickInterceptedException:
                try:
                    cancel_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel') or contains(text(), 'Cancelar')]")
                    cancel_btn.click()
                except NoSuchElementException:
                    pass

if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow(limit=1)