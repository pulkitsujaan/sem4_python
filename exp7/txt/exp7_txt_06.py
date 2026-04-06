# Experiment 7 - Section A - Program 6
# Count frequency of each word in a text file and display in descending order.

import re
from collections import Counter

def word_frequency(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # Extract words (ignore punctuation, case-insensitive)
        words = re.findall(r'\b[a-zA-Z]+\b', content.lower())

        if not words:
            print("No words found in the file.")
            return

        freq = Counter(words)
        sorted_freq = freq.most_common()

        print(f"\nWord Frequency in '{filename}' (Descending Order):")
        print(f"{'Word':<20} {'Count'}")
        print("-" * 30)
        for word, count in sorted_freq:
            print(f"{word:<20} {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the filename: ")
word_frequency(filename)
