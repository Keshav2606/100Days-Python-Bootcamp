import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://forms.gle/VtPexsz1fzQnr4JVA"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
zillow_website = response.text

soup = BeautifulSoup(zillow_website, "html.parser")

property_links = soup.find_all(name="a", class_="property-card-link")
property_links = [link.get("href") for link in property_links]
property_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
property_prices = [price.text.strip("+/mo 1bd") for price in property_prices]
property_addresses = soup.find_all(name="address")
property_addresses = [address.text.strip() for address in property_addresses]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

for i in range(len(property_links)):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(FORM_URL)

    time.sleep(3)

    q1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q1.send_keys(property_links[i])

    q2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q2.send_keys(property_prices[i])

    q3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q3.send_keys(property_addresses[i])

    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()

    driver.quit()
