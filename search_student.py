

import json

def search_student():
    print("\n--- Search Student ---")
    search_input = input("Enter ID or Contact: ")
    isfound = False

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for studentdict in data:
                # Match ID or Contact
                if (studentdict.get("id") == search_input or
                    studentdict.get("contact") == search_input):
                    print("Student Found:")
                    print(studentdict)
                    isfound = True
                    break

        if not isfound:
            print("No matching student found.")

    except FileNotFoundError:
        print("Student records not found!")