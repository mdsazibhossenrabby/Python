try:
    with open('data.txt','r') as source_file:
        content=source_file.read()
    with open('backup.text','w') as backup_file:
        backup_file.write(content)
except FileNotFoundError:
    print("The data.txt file is not exist")
except IOError:
    print("An error occurred while writing to backup.txt")