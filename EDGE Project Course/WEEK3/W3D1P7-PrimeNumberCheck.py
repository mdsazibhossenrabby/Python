


number=int(input("Enter A Number : " ))
if number<=1:
    print("Not Prime")
else:
    length=len(str(number))
    count=0
    for i in range(2,int(length/2) + 1):
        if number%i==0:
            count+=1
            break
    if count==0:
        print("Prime Number")
    else:
        print("Not Prime")
