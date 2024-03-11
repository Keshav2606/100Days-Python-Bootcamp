import requests
import smtplib
from bs4 import BeautifulSoup

my_email = "mishrag2606@gmail.com"
password = "jtduaeilnfnxbzeg"
product_url = "https://www.amazon.in/Noise-Launched-Display-Bluetooth-Calling/dp/B0C5DYKGCK/ref=sr_1_11_sspa?crid=1AHOBITC3IBXN&dib=eyJ2IjoiMSJ9.3opjQcJYPDRouFptdDgSNctz6QAi3zuE93xr6RkKcKR4nKHLRSflsqFfZSm7u01g_sUTUv2FkqAWqCBQaxljSv9bnECZILNaTmlQ-KLoNCLqD1AHWx_A8zXT8RNHES73ZkzZtu7ZQk0Y4qXPA7kQR5rJRotL7uSbBESBJTCN0QzehYZyxM-H0QNNoFd3TEqlXQnMzLEMx05zKrhW152Yily0d2xcMEft9AwowDXibqE.GKOtYdTLduwmqmSSf9CGwF4dQ5CxHtg_7RDpTfcK8BQ&dib_tag=se&keywords=boat+smart+watch&qid=1710081559&sprefix=boat+%2Caps%2C223&sr=8-11-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
}

response = requests.get(product_url, headers=headers)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
curr_price = soup.find(name="span", class_="a-price-whole").get_text()
curr_price = curr_price.replace(",", "")
curr_price = curr_price.replace(".", "")
curr_price = int(curr_price)

target_price = 2500

if curr_price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mishraji2606@gmail.com",
            msg="Subject:Price Drop Alert\n\nPrice of Noise Smartwatch dropped below ₹2400. You should buy it now.".encode("UTF-8")
        )
