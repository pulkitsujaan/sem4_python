# Experiment 7 - Section B - Program 2
# Calculate the average marks of students stored in a CSV file.

import csv

def average_marks(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            marks_list = []
            for row in reader:
                try:
                    marks_list.append(float(row['Marks']))
                except ValueError:
                    print(f"  Skipping invalid marks value for {row.get('Name', 'Unknown')}")

        if not marks_list:
            print("No valid marks data found.")
            return

        total = sum(marks_list)
        average = total / len(marks_list)

        print(f"\nFile          : {filename}")
        print(f"Total Students: {len(marks_list)}")
        print(f"Total Marks   : {total:.2f}")
        print(f"Average Marks : {average:.2f}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the CSV filename: ")
average_marks(filename)
