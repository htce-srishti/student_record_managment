import json
import os

def register_student():
    student = {}
    student['id'] = input("Enter ID: ")
    student['name'] = input("Enter Name: ")
    student['email'] = input("Enter Email: ")
    student['address'] = input("Enter Address: ")
    student['contact'] = input("Enter Contact Number: ")
    student['qualification'] = input("Enter Qualification: ")

    # Load existing data
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(student)

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student registered successfully!")