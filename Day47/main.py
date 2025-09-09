import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# URL of the product you want to monitor
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Header to simulate a real browser
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Get the website's HTML
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

# Get the price
price = soup.find(class_="a-offscreen").get_text()
# Remove the dollar sign and convert to float
price_as_float = float(price.replace("$", ""))
# Get the product title
title = soup.find(id="productTitle").get_text().strip()

# Price threshold for notification
BUY_PRICE = 70

# Check if the current price is below the threshold
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!\n{url}"

    # Send email
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject: Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
    print(f"Alert sent: {title} – Current price: {price} (Below ${BUY_PRICE})")
else:
    print(f"Checked: {title} – Current price: {price} (Above ${BUY_PRICE})")