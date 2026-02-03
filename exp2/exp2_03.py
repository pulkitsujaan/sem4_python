# Function to calculate total marks
def total_marks(marks_list):
    return sum(marks_list)

# Function to calculate percentage
def percentage(total):
    return total / 5   # since there are 5 subjects

# Function to calculate grade
def grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'Fail'


# Main program
marks = []

print("Enter marks of 5 subjects:")
for i in range(5):
    m = float(input(f"Subject {i+1}: "))
    marks.append(m)

total = total_marks(marks)
percent = percentage(total)
result_grade = grade(percent)

print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percent, "%")
print("Grade:", result_grade)
