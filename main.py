import requests
from datetime import datetime

APP_ID="Your NUTRITIONIX APP_ID"
API_KEY="Your NUTRITIONIX API_KEY"

NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "YOUR SHEETY url"


auth_header = {"Authorization": "Your Bearer Token"}
header = {
    "x-app-id" : APP_ID,
    "x-app-key" :API_KEY,
}

user_query = input("Tell Me which excercise you did? : ")
parameters = {
    "query": user_query
}

time = datetime.now()
today_date = time.strftime("%d/%m/%Y")
time_now = time.strftime("%H:%M:%S")
# print(today_date, time_now)


response = requests.post(url=NUTRITIONIX_API_ENDPOINT, headers=header, json=parameters)
response.raise_for_status()
data = response.json()
excersise_data = data["exercises"]


for exercise in excersise_data:
    calori_burn = exercise["nf_calories"]
    exercise_name = exercise["name"]
    excersice_duration = exercise["duration_min"]
    # print(f"Excercise : {exercise_name} \nDuration : {excersice_duration} \nCalories burnt : {calori_burn}")
    excersice_data = {
        "workout":{
            "date":today_date,
            "time": time_now,
            "exercise":exercise_name.title(),
            "duration": f"{int(excersice_duration)} min",
            "calories": calori_burn,
        }    
    }
    
    sheety_response = requests.post(url=SHEETY_URL, json=excersice_data, headers=auth_header) 
    sheety_response.raise_for_status()
    sheety_data = sheety_response.json()
    print(sheety_data)
    