# Experiment 7 - Section A - Program 8
# Read a file and display the longest word and shortest word.

import re

def find_longest_shortest(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()

        words = re.findall(r'\b[a-zA-Z]+\b', content)

        if not words:
            print("No words found in the file.")
            return

        longest = max(words, key=len)
        shortest = min(words, key=len)

        print(f"\nFile: '{filename}'")
        print(f"  Longest Word  : '{longest}' (length = {len(longest)})")
        print(f"  Shortest Word : '{shortest}' (length = {len(shortest)})")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the filename: ")
find_longest_shortest(filename)
