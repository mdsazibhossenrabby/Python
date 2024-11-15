#W3D2P2-

try:
    with open('note.txt','r') as nFile:
        content=nFile.read()
    with open('backup_notes.txt','w') as bnFile:
        bnFile.write(content)
except IOError:
    print("There is a problem while reading note.txt file")
except FileNotFoundError:
    print("There in not exist file")
