

number=int(input("Enter a number of multiplication table : "))
print(f"The Multiplication table of {number} : ")
for i in range(1,11):
    print(f"{number} * {i}  -> {number*i}")