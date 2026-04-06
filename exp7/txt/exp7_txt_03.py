# Experiment 7 - Section A - Program 3
# Copy contents of one text file to another, converting all lowercase to uppercase.

def copy_uppercase(source, destination):
    try:
        with open(source, 'r') as src:
            content = src.read()

        with open(destination, 'w') as dst:
            dst.write(content.upper())

        print(f"Contents copied from '{source}' to '{destination}' in uppercase.")

    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")

source = input("Enter the source filename: ")
destination = input("Enter the destination filename: ")
copy_uppercase(source, destination)
