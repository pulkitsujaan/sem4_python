# Experiment 7 - Section B - Program 3
# Search for a student record in a CSV file using roll number.

import csv

def search_student(filename, roll_no):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['RollNo'].strip() == str(roll_no).strip():
                    print("\nStudent Record Found:")
                    print("-" * 35)
                    print(f"  Roll No : {row['RollNo']}")
                    print(f"  Name    : {row['Name']}")
                    print(f"  Marks   : {row['Marks']}")
                    return

        print(f"No student found with Roll No: {roll_no}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the CSV filename: ")
roll_no = input("Enter Roll No to search: ")
search_student(filename, roll_no)
