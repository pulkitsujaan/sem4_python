# Experiment 7 - Section A - Program 5
# Remove all blank lines from a file and save the result into another file.

def remove_blank_lines(source, destination):
    try:
        with open(source, 'r') as f:
            lines = f.readlines()

        non_blank = [line for line in lines if line.strip() != '']
        removed = len(lines) - len(non_blank)

        with open(destination, 'w') as f:
            f.writelines(non_blank)

        print(f"Done! Removed {removed} blank line(s).")
        print(f"Output saved to '{destination}'.")

    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")

source = input("Enter the source filename: ")
destination = input("Enter the destination filename: ")
remove_blank_lines(source, destination)
