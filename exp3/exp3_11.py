while(True):
    x = input("Enter a number: ")
    if(x.isnumeric()):
        print("Valid input")
        break
    else:
        print("Not a valid input")
    