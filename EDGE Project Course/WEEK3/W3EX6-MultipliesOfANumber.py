

number=int(input("Enter a number : "))
print(f"Multiplies of {number} up to 100 : ")
for i in range(1,100) :
    if i%number==0 :
        print(i,end='')
print()