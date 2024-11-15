

with open('shopping_list.txt','r') as file:
    for position,line in enumerate(file,start=1):
        print(f"{position} : {line.strip()}")