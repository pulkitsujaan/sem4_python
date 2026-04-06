# Experiment 7 - Section B - Program 6
# Update marks of a specific student in a CSV file.

import csv

def update_marks(filename, roll_no, new_marks):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)

        updated = False
        for row in rows:
            if row['RollNo'].strip() == str(roll_no).strip():
                old_marks = row['Marks']
                row['Marks'] = str(new_marks)
                updated = True
                print(f"\nStudent '{row['Name']}' (Roll No: {roll_no})")
                print(f"  Marks updated: {old_marks} --> {new_marks}")
                break

        if not updated:
            print(f"No student found with Roll No: {roll_no}")
            return

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"File '{filename}' updated successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the CSV filename: ")
roll_no = input("Enter Roll No of student to update: ")
new_marks = input("Enter new Marks: ")
update_marks(filename, roll_no, new_marks)
