

number=int(input("Enter a number : "))
isPrime=True
if number>1:
    for i in range(2,int(number**0.5)+1) :
        if number%i==0:
            isPrime=False
            break
    if isPrime:
        print(f"The number {number} is a Prime number ")
    else :
        print(f"The number {number} is not a Prime number ")
else :
    print(f"The number {number} is not a Prime number ")