def unique_values(*args):
    seen = set()
    result = []
    
    for value in args:
        if value not in seen:
            seen.add(value)
            result.append(value)
    
    return result


# Example usage
print(unique_values(1, 2, 2, 3, 4, 3, 5))
print(unique_values("a", "b", "a", "c", "b"))


'''

[1, 2, 3, 4, 5]
['a', 'b', 'c']

'''