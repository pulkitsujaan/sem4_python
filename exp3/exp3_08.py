# Program to sort a list based on last digit using lambda

numbers = list(map(int, input("Enter integers separated by space: ").split()))

sorted_list = sorted(numbers, key=lambda x: x % 10)

print("Sorted list based on last digit:")
print(sorted_list)
