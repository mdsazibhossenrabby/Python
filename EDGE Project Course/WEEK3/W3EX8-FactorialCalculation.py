

number=int(input("Enter a non-negative number : "))
factorial=1
for i in range(1,number+1):
    factorial*=i
print(f"The Factorial of {number} is {factorial} ")