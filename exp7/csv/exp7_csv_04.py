# Experiment 7 - Section B - Program 4
# Read a CSV file and display students who scored above a given threshold.

import csv

def students_above_threshold(filename, threshold):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            results = []
            for row in reader:
                try:
                    if float(row['Marks']) > threshold:
                        results.append(row)
                except ValueError:
                    pass

        if results:
            print(f"\nStudents scoring above {threshold} marks:")
            print(f"{'RollNo':<10} {'Name':<20} {'Marks'}")
            print("-" * 40)
            for row in results:
                print(f"{row['RollNo']:<10} {row['Name']:<20} {row['Marks']}")
            print(f"\nTotal: {len(results)} student(s)")
        else:
            print(f"No students found with marks above {threshold}.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the CSV filename: ")
threshold = float(input("Enter the marks threshold: "))
students_above_threshold(filename, threshold)
