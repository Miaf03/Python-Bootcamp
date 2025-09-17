import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

all_links = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]
all_addresses = [addr.get_text().replace(" | ", " ").strip() for addr in soup.select(".StyledPropertyCardDataWrapper address")]
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in soup.select(".PropertyCardWrapper span") if "$" in price.text]

print(f"Scraping completo: {len(all_links)} links, {len(all_addresses)} direcciones, {len(all_prices)} precios")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(3):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )

    price_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_field = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()

    time.sleep(1)

time.sleep(5)
driver.quit()