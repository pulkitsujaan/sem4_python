def get_positive_number():
    while True:
        try:
            num = int(input("Enter a non-negative number: "))
            
            if num < 0:
                raise Exception("Negative numbers are not allowed.")
            
            print("Valid number entered:", num)
            break   # Exit loop when valid
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        
        except Exception as e:
            print("Error:", e)


# Call the function
get_positive_number()
