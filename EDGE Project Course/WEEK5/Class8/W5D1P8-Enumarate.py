

def PrintList(numbers):
    for i,n in enumerate(numbers,start=1):
        print(f"{i}. {n}")
        
numbers=[i*3 for i in range(1,11)]
PrintList(numbers)