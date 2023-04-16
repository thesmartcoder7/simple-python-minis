import requests
from datetime import datetime
from constants import *

exercise_endpoint = "your workout api"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

headers.update(BEARER)

today = datetime.now()
date = today.date().strftime("%d/%m/%Y")
time = today.time().strftime("%X")

workout = input("what exercises did you do for the day?: ")
answer = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=exercise_endpoint, json=answer, headers=headers)
response.raise_for_status()
exercises = response.json()["exercises"]
sheety_data = {
    "workout": {
        "date": "",
        "time": "",
        "exercise": "",
        "duration": "",
        "calories": ""
    }
}

for exercise in exercises:
    sheety_data["workout"]["date"] = date
    sheety_data["workout"]["time"] = time
    sheety_data["workout"]["exercise"] = exercise['name'].title()
    sheety_data["workout"]["duration"] = str(round(exercise['duration_min']))
    sheety_data["workout"]["calories"] = str(round(exercise['nf_calories']))

    post_response = requests.post(url=POST_ENDPOINT, json=sheety_data, headers=headers)
    post_response.raise_for_status()


print(post_response.text)
