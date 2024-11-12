

n=int(input("Enter a number : "))
total=sum(i for i in range(1,n+1) if i%2!=0)
print(f"The sum of odd numbers from 1 to {n} id {total}")