x = 50   # Global variable

def display(x):   # Parameter has same name as global variable
    print("Inside function, x =", x)

print("Global x before function call =", x)

display(100)   # Passing argument to function

print("Global x after function call =", x)
