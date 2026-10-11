print("Task 1")

def shopping_list(items):
    with open("shopping_list.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(f"{item}\n")
    return

shopping_list(["Milk", "Cheese", "Bread", "Apples"])

with open("shopping_list.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("Task 2")

import csv
from os import write

with open("students.csv", "w", encoding="utf-8",newline="") as init_file:
    init_file.write("name,age\nAnna,21\nTom,19\nKate,22\n")

def read_students(filename):
    with open(filename,"r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")
    return

read_students("students.csv")

print("Task 3")


import json


def save_profile(name, age, city):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }
    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)  # indent=4 - отступы
    return

save_profile("Vera", 27 ,"Haifa")


print("Task 4")
from pathlib import Path

data_folder = Path("data_test")
file_path = data_folder / "test.csv"
print(file_path)

print(file_path.exists())

screen_folder = Path("screen")
screen_folder.mkdir(exist_ok=True)
reports_folder = Path("reports")/"october"
reports_folder.mkdir(parents=True, exist_ok=True)

print("Task 5")

from pathlib import Path

def create_reports_folder():
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    results_file = reports_dir / "result.txt"
    with open(results_file, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!\n")
    return

create_reports_folder()