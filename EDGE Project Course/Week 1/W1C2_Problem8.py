
Size=int(input("Enter List Size : "))

Array = list(map(int,input("\nEnter the numbers : ").split()))[:Size]

print(f"The Max Value is {max(Array)},Minimum Value is {min(Array)} and Sum of all value is {sum(Array)}")