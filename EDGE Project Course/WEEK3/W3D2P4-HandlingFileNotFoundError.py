
try:
    with open('grocery_list.txt','r') as gFile:
        content=gFile.read()
except FileNotFoundError:
    print("The file grocery_list.txt is not exist")