import requests
from datetime import datetime
from tkinter import *
EXERCISE_TEXT = ""

def get_input():
    output = workout_entry.get()
    EXERCISE_TEXT = output
    
    nutri_app_id = "APP_ID"
    nutri_api_key = "APP_TOKEN"
    gender = "GENDER"
    weight_kg = 80
    height_cm = 250
    age = 23

    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    exercise_header = {
        "x-app-id": nutri_app_id,
        "x-app-key": nutri_api_key, }
    exercise_params = {
        "query": EXERCISE_TEXT,
        "gender": gender,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age,
    }

    spreadsheet_auth_endpoint = "https://api.sheety.co/4d13843d6e296143258a6c5ec1f16284/ireneWorkout/workouts"

    today_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%X")

    response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_header)
    result = response.json()
    print(result)

    for exercise in result["exercises"]:
        data = {"workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["user_input"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": exercise["nf_calories"],

        }, }
        if int(data["workout"]["duration"]) > 563:
            label = Label(text="Is that possible ???", bg="#CCB7D4")
            label.grid(column=0, row=3, columnspan=2, pady=30)
            print()
        response = requests.post(url=spreadsheet_auth_endpoint, json=data)
        response.json()
    workout_label.config(text="")
    print("Successful")


