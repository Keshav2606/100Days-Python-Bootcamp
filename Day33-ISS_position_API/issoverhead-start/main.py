import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.678841
MY_LONG = -84.498482


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead():
        if is_night():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="mishrag2606@gmail.com", password="jtduaeilnfnxbzeg")
                connection.sendmail(
                    from_addr="mishrag2606@gmail.com",
                    to_addrs="mishraji2606@gmail.com",
                    msg="Subject:ISS Overhead\n\nLookup, ISS is currently over your head."
                )
        else:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="mishrag2606@gmail.com", password="jtduaeilnfnxbzeg")
                connection.sendmail(
                    from_addr="mishrag2606@gmail.com",
                    to_addrs="mishraji2606@gmail.com",
                    msg="Subject:ISS Overhead\n\nISS is currently over your head, but you can't see it because of daylight."
                )
