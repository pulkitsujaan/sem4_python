def find_max(lst, index=0, current_max=None):
    if not lst:
        return None
    
    # Initialize current_max during first call
    if current_max is None:
        current_max = lst[0]
    
    # Base case: reached end of list
    if index >= len(lst):
        return current_max
    
    # Indirect recursive call
    return max_helper(lst, index, current_max)


def max_helper(lst, index, current_max):
    if lst[index] > current_max:
        current_max = lst[index]
    
    # Call first function again (indirect recursion)
    return find_max(lst, index + 1, current_max)


# Example usage
numbers = [3, 12, 5, 99, 34, 76]
print(find_max(numbers))   # Output: 99
