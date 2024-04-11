import requests
import smtplib
from datetime import datetime
import time

MY_LATS = 3.139003
MY_LONG = 101.686852
MY_EMAIL = "kucknien@yahoo.com"
MY_PASSWORD = "fvzsftxabdxdiisr"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()['iss_position']
    iss_longitude = float(data['longitude'])
    iss_latitude = float(data['latitude'])

    if MY_LATS-5 <= iss_latitude <= MY_LATS+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LATS,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="kucknien@gmail.com",
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky"
            )