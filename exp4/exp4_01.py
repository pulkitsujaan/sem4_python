def find_max(*numbers):
    if not numbers:   # handle case when no arguments are passed
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num


# Taking input from user
nums = input("Enter numbers separated by space: ").split()

# Convert input strings to integers
nums = [int(num) for num in nums]

# Calling the function
maximum = find_max(*nums)

# Printing result
if maximum is not None:
    print("The maximum number is:", maximum)
else:
    print("No numbers were provided.")