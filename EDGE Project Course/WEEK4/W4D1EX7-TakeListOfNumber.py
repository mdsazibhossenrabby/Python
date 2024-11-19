

def sumOFevenNumbers(numbers):
    return sum(n for n in numbers if n%2==0)

numbers=list(map(int,input("Enter Numbers : ").split()))

print(f"The sum of the even numbers : {sumOFevenNumbers(numbers)}")