# Experiment 7 - Section B - Program 7
# Count how many students passed (marks >= 40) and failed from a CSV file.

import csv

def count_pass_fail(filename, passing_marks=40):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            passed = []
            failed = []

            for row in reader:
                try:
                    marks = float(row['Marks'])
                    if marks >= passing_marks:
                        passed.append(row)
                    else:
                        failed.append(row)
                except ValueError:
                    print(f"  Skipping invalid entry: {row}")

        total = len(passed) + len(failed)

        print(f"\nFile          : {filename}")
        print(f"Passing Marks : {passing_marks}")
        print(f"Total Students: {total}")
        print(f"Passed        : {len(passed)}")
        print(f"Failed        : {len(failed)}")

        if failed:
            print("\nFailed Students:")
            print(f"  {'RollNo':<10} {'Name':<20} {'Marks'}")
            print("  " + "-" * 38)
            for row in failed:
                print(f"  {row['RollNo']:<10} {row['Name']:<20} {row['Marks']}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the CSV filename: ")
count_pass_fail(filename)
