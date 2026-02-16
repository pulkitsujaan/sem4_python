def toggle_case(text):
    result = ""
    
    for ch in text:
        ascii_value = ord(ch)
        
        # Check if character is alphabetic (A-Z or a-z)
        if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
            # Toggle case using bitwise XOR with 32
            toggled_char = chr(ascii_value ^ 32)
            result += toggled_char
        else:
            # Keep non-alphabetic characters unchanged
            result += ch
    
    return result


# Taking input from user
user_input = input("Enter a string: ")
print("Toggled string:", toggle_case(user_input))


'''
Input:  Hello World! 123
Output: hELLO wORLD! 123
'''