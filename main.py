from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import time

MY_EMAIL = "ocktosh1968@gmail.com"
TO_EMAIL = "ghostjogger@gmail.com"
MY_PASSWORD = "19meikle78"
URL = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5+console&qid=1615808593&sr=8-1"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.146 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

while True:
    response = requests.get(url=URL, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, "lxml")
    title = soup.find(id="productTitle").get_text().strip()
    print(title)
    price = soup.find(id="desktop_unifiedPrice").text.split()
    try:
        print(price[1])
    except IndexError:
        print("Not available yet!")
    else:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:PS5 console available now!\n\nGet it now from Amazon"
            )
    time.sleep(5)
