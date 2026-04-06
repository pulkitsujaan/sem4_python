# Experiment 7 - Section A - Program 2
# Read a file and print only those lines that contain a specific keyword.

def search_keyword(filename, keyword):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        matched = [line.rstrip() for line in lines if keyword.lower() in line.lower()]

        if matched:
            print(f"\nLines containing '{keyword}':")
            print("-" * 40)
            for i, line in enumerate(matched, 1):
                print(f"{i}: {line}")
        else:
            print(f"No lines found containing the keyword '{keyword}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the filename: ")
keyword = input("Enter the keyword to search: ")
search_keyword(filename, keyword)
