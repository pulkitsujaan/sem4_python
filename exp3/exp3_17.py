# Function to return only positive numbers using lambda and filter
def get_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


# Main program
nums = list(map(int, input("Enter integers separated by space: ").split()))

positive_nums = get_positive_numbers(nums)

print("Positive numbers:", positive_nums)
