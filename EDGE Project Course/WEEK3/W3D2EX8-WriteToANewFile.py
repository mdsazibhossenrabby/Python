
with open('number.txt','w') as file:
    for number in range(1,11):
        file.write(f"{number}\n")