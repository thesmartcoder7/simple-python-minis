from bs4 import BeautifulSoup
import requests
import smtplib

product_url = "https://www.amazon.com/WALI-Free-Standing-Adjustable-Capacity-MF003/dp/B07GBL3PN3/ref=sr_1_18?keywords" \
              "=triple+monitor+mount&qid=1639953207&sr=8-18"  # the url of the product you are eyeing goes here
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
    # there headers are easily found on "http://myhttpheader.com/"
}

response = requests.get(url=product_url, headers=headers)
response.raise_for_status()
product_page = response.text

soup = BeautifulSoup(product_page, features="html.parser")
# you can use lxml too if html.parser doesn't work

product_price = float(soup.select(selector=".a-price")[0].select(selector=".a-offscreen")[0].text.replace("$", ""))

desired_price = 45.00
# your desired price on amazon after checking the price fluctuations on camelcamelcamel.com

if product_price < desired_price:
    with smtplib.SMTP("your domain name/ smtp name") as connection:
        username = "sender email"
        password = "sender password"
        recipient = "recepient email"
        message = f"The price of WALI Triple LCD Monitor Desk Mount Fully Adjustable Horizontal Stand (Black)" \
                  f" is below ${desired_price}0. Buy Now!! "
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=recipient, msg=f"Subject: Price Just Right! \n{message}")

    print("Alert sent successfully!!")
