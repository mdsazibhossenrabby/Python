
number=int(input("Enter a positive number : "))
length=len(str(number))
sum=0
for i in range(length):
    temp=number%10
    sum=sum+temp
    number=int(number/10)
print(f"The sum of the all digits is {sum}")