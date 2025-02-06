from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from typing import Union
import json
import os
from datetime import datetime
import random
from studentvue import StudentVue

# TODO: add location guessing game

app = FastAPI()
param = "-n" if os.name == "nt" else "-c"
sv = StudentVue(
    ">REDACTED",
    ">REDACTED",
    "https://mn-mvps-psv.edupoint.com/PXP2_Login_Student.aspx",
)


@app.get("/jfin")
def ping_jfin():
    response = os.system(f"ping {param} 1 127.0.0.1")
    if response == 0:
        return "my jellyfin server is up!"
    else:
        return "my jellyfin server is down!"


@app.get("/time")
def return_time():
    current_time = datetime.now()
    if current_time.strftime("%H:%M") == "7:00":
        return "IT'S 7:00!"
    else:
        return f"It is {current_time}"


@app.get("/where")
def where_is_bro():
    current_time = datetime.now()
    day = current_time.strftime("%w")
    hour = int(current_time.strftime("%H"))

    schedule = {
        "1": [
            (8, 17, "bro is at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 21, "at home, probably online"),
        ],
        "3": [
            (8, 17, "bro is at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 21, "at home, probably online"),
        ],
        "5": [
            (8, 17, "bro is at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 21, "at home, probably online"),
        ],
        "2": [
            (8, 15, "bro is at school"),
            (18, 21, "bro is back at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 18, "at home, probably online"),
        ],
        "4": [
            (8, 15, "bro is at school"),
            (18, 21, "bro is back at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 18, "at home, probably online"),
        ],
        "6": [
            (8, 15, "bro is at school again"),
            (18, 21, "bro is back at school"),
            (21, 6, "am sleep, probably won't respond"),
            (6, 18, "at home, probably online"),
        ],
        "0": [
            (21, 6, "am sleep, probably won't respond"),
            (6, 21, "at home, probably online"),
        ],
    }

    for start, end, message in schedule.get(day, []):
        if start <= hour < end or (start > end and (hour >= start or hour < end)):
            return message

    return "at home, probably online"


@app.get("/yap")
def get():
    with open("yap.json", "r") as file:
        data = json.load(file)
        yap = random.choice(data)
    return {"yap:": f"{yap}"}


@app.get("/grades", response_class=PlainTextResponse)
def get_grades():
    sv = StudentVue(
        "sigmauser",
        "massivepassword",
        "https://mn-mvps-psv.edupoint.com/PXP2_Login_Student.aspx",
    )
    grades = sv.get_gradebook()
    grades = grades["Gradebook"]["Courses"]["Course"]
    response = ""
    for key in grades:
        response += f"\nPeriod {key["@Period"]}: {key["@CourseName"]} with {key["@Staff"]}. Grade: {key["Marks"]["Mark"]["@CalculatedScoreRaw"]} ({key["Marks"]["Mark"]["@CalculatedScoreString"]})"
    print(response)
    return response


@app.post("/grades", response_class=PlainTextResponse)
def get_other_grades(user: str, password: str):
    sv = StudentVue(
        user,
        password,
        "https://mn-mvps-psv.edupoint.com/PXP2_Login_Student.aspx",
    )
    grades = sv.get_gradebook()
    grades = grades["Gradebook"]["Courses"]["Course"]
    response = ""
    for key in grades:
        response += f"\nPeriod {key["@Period"]}: {key["@CourseName"]} with {key["@Staff"]}. Grade: {key["Marks"]["Mark"]["@CalculatedScoreRaw"]} ({key["Marks"]["Mark"]["@CalculatedScoreString"]})"
    print(response)
    return response


@app.post("/yap")
def submit_yap(yap_submission: str):
    with open("yap.json", "r") as file:
        data = json.load(file)
        data.append(yap_submission)
    with open("yap.json", "w") as file:
        json.dump(data, file)
    return {"message": "yap submitted"}
