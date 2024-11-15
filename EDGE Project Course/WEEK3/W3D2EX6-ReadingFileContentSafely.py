

try:
    with open('data.txt','r') as file:
        content=file.read()
        print(content)
except IOError:
    print("An error occurred while reading the file")