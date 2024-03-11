from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_input = driver.find_element(By.NAME, value="fName")
lname_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")

fname_input.send_keys("Keshav")
lname_input.send_keys("Mishra")
email_input.send_keys("keshav.mishra2606@gmail.com")
button.click()

