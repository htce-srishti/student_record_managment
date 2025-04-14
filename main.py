import json
import os

from student_registration import register_student
from display_all_record import display_all_students
from search_student import search_student
 
def menu():
    while True:
        print("\n===== Student Record Management =====")
        print("1. Register Student")
        print("2. Display All Students")
        print("3. Search Student (by Email or Contact)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            register_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again!")

menu()