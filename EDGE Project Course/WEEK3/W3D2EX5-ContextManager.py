

#Without Context Manager
file=open('data.txt','r')
content1=file.read()
file.close()

#With Context Manager
with open('data.txt','r') as file:
    content2 = file.read()