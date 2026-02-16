def custom_slice(text, start, end):
    result = ""
    
    # Handle negative indices (basic support)
    if start < 0:
        start = len(text) + start
    if end < 0:
        end = len(text) + end

    # Ensure indices are within bounds
    start = max(0, start)
    end = min(len(text), end)

    for i in range(start, end):
        result += text[i]
    
    return result


# Example usage
print(custom_slice("Hello World", 0, 5))    # Hello
print(custom_slice("Hello World", 6, 11))   # World
print(custom_slice("Python", -4, -1))       # tho
