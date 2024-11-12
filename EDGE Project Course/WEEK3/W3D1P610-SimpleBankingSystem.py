balance=0.0

while 1==1:
    print("1. Deposit\n"
          "2. Balance Check\n"
          "3. Withdraw\n"
          "4. Exit\n")
    option=int(input("Enter Option : "))
    if option==1:
        depo=float(input("Enter Deposit Amount : "))
        balance+=depo
        print(f"{depo} deposit successful \n")
    elif option == 2:
        print(f"The Balance : {balance} \n")
    elif option == 3:
        withdraw=float(input("Enter Withdraw Amount : "))
        if withdraw>balance:
            print("Insufficient Balance\n")
        else:
            balance-=withdraw
            print(f"{withdraw} withdraw is successful\n")
    elif option==4:
        print("System is Turned off\n")
        break
    else:
        print("Wrong Option, Try Again")