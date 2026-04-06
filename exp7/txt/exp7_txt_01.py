# Experiment 7 - Section A - Program 1
# Count number of lines, words, and characters in a given text file.

def count_file_stats(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    print(f"File: {filename}")
    print(f"  Number of Lines      : {num_lines}")
    print(f"  Number of Words      : {num_words}")
    print(f"  Number of Characters : {num_chars}")

filename = input("Enter the filename: ")
count_file_stats(filename)