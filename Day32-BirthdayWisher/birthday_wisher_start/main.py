# 1. Update the birthdays.csv
import pandas as pd
import datetime as dt
import smtplib
import random

data = pd.read_csv("./birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
day = today.day
month = today.month
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_mail = "mishrag2606@gmail.com"
password = "jtduaeilnfnxbzeg"

for data in data_dict:
    if int(data["month"]) == month and int(data["day"]) == day:
        birthday_person = data
        letter = random.choice(letters)
        with open(f"./letter_templates/{letter}", mode="r") as letter_file:
            letter_content = letter_file.read()
            new_letter_content = letter_content.replace("[NAME]", data["name"])

        receiver_mail = birthday_person["email"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_mail, password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=receiver_mail,
                msg=f"Subject:Happy Birthday!!\n\n{new_letter_content}"
            )
