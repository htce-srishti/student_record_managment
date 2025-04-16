

import json
import os

def display_all_students():
    print("\n--- All Student Records ---")
    try:
        with open("students.json", "r") as f:
            records = json.load(f)  # use json.load to parse JSON properly

        if records:
            for data in records:
                print(f"ID: {data['id']}, Name: {data['name']}, Email: {data['email']}, Address: {data['address']}, Contact: {data['contact']}, Qualification: {data['qualification']}")
        else:
            print("No records found.")
    except FileNotFoundError:
        print("students.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file. Please check the file format.")

