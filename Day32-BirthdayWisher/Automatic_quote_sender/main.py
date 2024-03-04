import random
import smtplib
import datetime as dt
from twilio.rest import Client

my_email = "mishrag2606@gmail.com"
password = "jtduaeilnfnxbzeg"

account_sid = "ACf37f08a539c79e7e968db1983fb4ae02"
auth_token = ""

today = dt.datetime.now()
hour = today.hour

if hour > 7:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        with open("quotes.txt", mode="r") as quotes_file:
            quotes = quotes_file.readlines()
            quote = random.choice(quotes)

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nakulsatyawali123@gmail.com",
            msg=f"Subject:Motivational quote\n\n{quote}\nby:- Keshav Mishra"
        )

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="+14067408619",
            body=f"{quote}\nby:- Keshav Mishra",
            to="+918178753778"
        )

        print(message.status)
