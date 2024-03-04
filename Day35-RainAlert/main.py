import requests
from twilio.rest import Client

city = "London"
API_KEY = "3cecebe712ffca4aca1213818b57a8a1"

account_sid = "ACf37f08a539c79e7e968db1983fb4ae02"
auth_token = "a4a52cdee2d7dd99e29ede8c367641b0"

parameters = {
    "q": city,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

day_data = response.json()["list"]

will_rain = False
for hour_data in day_data:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+14067408619",
        body="It'll gonna rain today. So, went outside with an Umbrella",
        to="+918178753778"
    )

    print(message.status)
