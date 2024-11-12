

n=int(input("Enter number of terms in Fibonacci sequence : "))
first,second=0,1
print("Fibonacci sequence : ")
for _ in range(n) :
    print(first,end=' ')
    first,second=second,first+second
print()

