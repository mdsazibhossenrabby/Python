

Range=int(input("Enter the range of even numbers (0 - 100): "))

for i in range(1,Range):
    if i%2==0:
        print(i,end='')
    print()