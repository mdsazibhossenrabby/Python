

def Factorial(n):
    if n==0:
        return 1
    else :
        return n*Factorial(n-1)

print(f"The Factorial of 5 is : {Factorial(5)}")