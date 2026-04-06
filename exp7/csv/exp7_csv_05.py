# Experiment 7 - Section B - Program 5
# Sort CSV records based on marks and write sorted data into a new file.

import csv

def sort_by_marks(source, destination, descending=True):
    try:
        with open(source, 'r') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)

        sorted_rows = sorted(rows, key=lambda x: float(x['Marks']), reverse=descending)

        with open(destination, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)

        order = "Descending" if descending else "Ascending"
        print(f"\nRecords sorted by Marks ({order}) and saved to '{destination}'.")
        print(f"\n{'RollNo':<10} {'Name':<20} {'Marks'}")
        print("-" * 40)
        for row in sorted_rows:
            print(f"{row['RollNo']:<10} {row['Name']:<20} {row['Marks']}")

    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
    except ValueError as e:
        print(f"Error parsing marks: {e}")

source = input("Enter the source CSV filename: ")
destination = input("Enter the destination CSV filename: ")
order = input("Sort order - Enter 'd' for Descending, 'a' for Ascending: ").strip().lower()
sort_by_marks(source, destination, descending=(order != 'a'))
