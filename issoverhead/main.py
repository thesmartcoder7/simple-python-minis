import requests
from datetime import datetime
import smtplib
import time

# for a later project, make these dynamic by using geolocation.
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def iss_is_close():
    result = requests.get(url="http://api.open-notify.org/iss-now.json")
    result.raise_for_status()
    result = result.json()

    iss_latitude = float(result["iss_position"]["latitude"])
    iss_longitude = float(result["iss_position"]["longitude"])

    if (MY_LAT - float(5)) <= iss_latitude <= (MY_LAT + float(5)) and \
            (MY_LONG - float(5)) <= iss_longitude <= (MY_LONG + float(5)):
        return True


def it_is_dark():
    time_now = datetime.now()
    location_parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=location_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(300000)  # this is to ensure that this program checks every 5 minutes
    if iss_is_close() and it_is_dark():
        sender = "your email"
        password = "your password"
        receiver = "recipient's password"
        subject = "The ISS Report!"
        with smtplib.SMTP("your smtp name / domain name") as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=receiver,
                msg=f"Subject: {subject}\n\nThe ISS is flying by. Get out and watch it go! Have fun."
            )
            print("Email has been successfully sent!")
