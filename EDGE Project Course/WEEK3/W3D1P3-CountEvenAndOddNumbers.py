

number=None
countEven=0
countOdd=0
while(1==1):
    number=int(input("Enter Number : "))
    if number==0:
        break
    elif number%2==0:
        countEven+=1
    else:
        countOdd+=1
print(f"There are {countEven} even numbers and {countOdd} odd numbers")