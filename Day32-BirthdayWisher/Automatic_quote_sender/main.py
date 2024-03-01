import random
import smtplib
import datetime as dt

my_email = "mishrag2606@gmail.com"
password = "jtduaeilnfnxbzeg"

today = dt.datetime.now()
hour = today.hour

if hour == 8:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        with open("quotes.txt", mode="r") as quotes_file:
            quotes = quotes_file.readlines()
            quote = random.choice(quotes)

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nakulsatyawali123@gmail.com",
            msg=f"Subject:Motivational quote\n\n{quote}"
        )


