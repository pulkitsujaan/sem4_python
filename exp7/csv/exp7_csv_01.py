# Experiment 7 - Section B - Program 1
# Create a CSV file of students (Roll No, Name, Marks) and read & display the data.

import csv
import os

FILENAME = "students.csv"

def create_csv():
    n = int(input("How many student records to add? "))
    rows = []
    for i in range(n):
        roll = input(f"  Roll No [{i+1}]: ")
        name = input(f"  Name    [{i+1}]: ")
        marks = input(f"  Marks   [{i+1}]: ")
        rows.append([roll, name, marks])

    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["RollNo", "Name", "Marks"])
        writer.writerows(rows)

    print(f"\nData written to '{FILENAME}' successfully.")

def read_csv():
    try:
        with open(FILENAME, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            print("No records found.")
            return

        print(f"\n{'RollNo':<10} {'Name':<20} {'Marks'}")
        print("-" * 40)
        for row in rows:
            print(f"{row['RollNo']:<10} {row['Name']:<20} {row['Marks']}")

    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. Please create the file first.")

print("1. Create CSV File")
print("2. Read & Display CSV File")
print("3. Both (Create then Display)")
choice = input("Enter choice: ")

if choice == '1':
    create_csv()
elif choice == '2':
    read_csv()
elif choice == '3':
    create_csv()
    read_csv()
else:
    print("Invalid choice.")
