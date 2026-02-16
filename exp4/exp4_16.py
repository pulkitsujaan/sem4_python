x = 10   # Global variable

def modify():
    x = 20   # Attempt to modify global variable
    print("Inside function, x =", x)

print("Before function call, x =", x)
modify()
print("After function call, x =", x)
