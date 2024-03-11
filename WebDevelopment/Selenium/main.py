from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
product_url = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(product_url)

python_events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
python_events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")

events_info = {}
for i in range(len(python_events_time)):
    events_info[i] = {
        "time": python_events_time[i].text,
        "name": python_events_name[i].text
    }

print(events_info)

driver.quit()
