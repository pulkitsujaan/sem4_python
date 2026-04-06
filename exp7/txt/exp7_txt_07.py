# Experiment 7 - Section A - Program 7
# Merge two text files line by line into a third file.

def merge_files(file1, file2, output):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        max_len = max(len(lines1), len(lines2))

        with open(output, 'w') as fout:
            for i in range(max_len):
                if i < len(lines1):
                    fout.write(lines1[i].rstrip('\n') + '\n')
                if i < len(lines2):
                    fout.write(lines2[i].rstrip('\n') + '\n')

        print(f"Files '{file1}' and '{file2}' merged successfully into '{output}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")

file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")
output = input("Enter the output filename: ")
merge_files(file1, file2, output)
