def find_max(*numbers):
    if not numbers:   # handle case when no arguments are passed
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num
