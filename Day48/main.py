import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")

end_time = time.time() + 60 * 5
while time.time() < end_time:
    cookie.click()

    if int(time.time()) % 10 == 0:
        precios = [
            int(item.text.split("-")[1].strip().replace(",", ""))
            for item in store_items if item.text != ""
        ]
        galletas_actuales = int(
            driver.find_element(By.ID, "cookies").text.split()[0].replace(",", "")
        )
        asequibles = [
            item for item, precio in zip(store_items, precios)
            if precio <= galletas_actuales
        ]
        if asequibles:
            asequibles[-1].click()

driver.quit()