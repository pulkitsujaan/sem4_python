from functools import reduce

def find_max(lst):
    if not lst:   # Handle empty list
        return None
    
    return reduce(lambda x, y: x if x > y else y, lst)


# Example usage
numbers = [10, 45, 3, 99, 27]
maximum = find_max(numbers)

print(maximum)


# Output: 99