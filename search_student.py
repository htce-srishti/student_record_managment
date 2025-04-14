import json 
import os

def search_student():
    print("\n--- Search Student ---")
    keyword = input("Enter email or contact to search: ").lower()
    found = False

    try:
        with open("students.json", "r") as f:
            for line in f:
                if keyword in line.lower():
                    data = line.strip().split(",")
                    print(f"ID: {data[0]}, Name: {data[1]}, Email: {data[2]}, Address: {data[3]}, Contact: {data[4]}, Qualification: {data[5]}")
                    found = True
        if not found:
            print("No matching student found.")
    except FileNotFoundError:
        print("Student records not found!")