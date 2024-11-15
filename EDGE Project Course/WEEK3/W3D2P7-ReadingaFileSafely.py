

try:
    with open('note.txt','r') as nFile:
        content=nFile.read()
        print(content)
except IOError:
    print("There is a problem while reading file")