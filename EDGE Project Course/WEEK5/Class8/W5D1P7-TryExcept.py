

nstring = input("Enter a Number : ")

try:
    
    n = int(nstring)
    print("Converted")
except ValueError:
    print("The String is not a numeric string")  # The input is not a valid integer
