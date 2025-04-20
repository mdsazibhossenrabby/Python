n=int(input("Enter A Number : "))

if(n>5):
    print(f"The Reduce Vale is : {n-2}")
elif(n==5):
    print(f"The Value is {0}")
else:
    print(f"The Increased Value is {n+5}")
    
# in logical operator
var1=input("Entert Your Name : ")
if("MD" or "Mohammad" or "md" or "mohammad"  in var1) :
    print("The person is Muslim")
else:
    print("The Person is not muslim")