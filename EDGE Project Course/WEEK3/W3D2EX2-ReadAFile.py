

with open('data.txt','r') as file:
    for lineNumber,lines in enumerate(file,start=3): #i can pass 0,1,2 as i want in start
        print(f"Line {lineNumber} : {lines.strip()}")
