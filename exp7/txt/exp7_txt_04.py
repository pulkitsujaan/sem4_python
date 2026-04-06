# Experiment 7 - Section A - Program 4
# Find and replace all occurrences of a word in a file with another word.

def find_and_replace(filename, old_word, new_word):
    try:
        with open(filename, 'r') as f:
            content = f.read()

        count = content.lower().count(old_word.lower())

        if count == 0:
            print(f"Word '{old_word}' not found in the file.")
            return

        # Case-insensitive replacement preserving structure
        import re
        updated = re.sub(re.escape(old_word), new_word, content, flags=re.IGNORECASE)

        with open(filename, 'w') as f:
            f.write(updated)

        print(f"Replaced {count} occurrence(s) of '{old_word}' with '{new_word}' in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the filename: ")
old_word = input("Enter the word to find: ")
new_word = input("Enter the replacement word: ")
find_and_replace(filename, old_word, new_word)
