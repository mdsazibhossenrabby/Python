
try:
    with open('datam.txt','r') as file:
        fileContent=file.read()
except FileNotFoundError:
    print("The file not Found")