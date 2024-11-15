#W3D2EX1-CreatFile

with open('data.txt','r') as file:
    lineCount=sum(1 for line in file)
    print(f"Total Number of Line in the file : {lineCount}")