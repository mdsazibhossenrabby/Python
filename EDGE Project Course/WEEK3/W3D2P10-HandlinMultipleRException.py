try:
    with open('note.txt','r') as nFile:
        content=nFile.read()
except IOError:
    print("There is a problem while reading note.txt file")
except FileNotFoundError:
    print("There in not exist file")