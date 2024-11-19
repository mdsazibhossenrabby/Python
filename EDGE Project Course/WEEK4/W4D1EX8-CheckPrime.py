

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

print(f"Is 15 is Prime number : {isPrime(15)}")
print(f"Is 11 is Prime number : {isPrime(11)}")
