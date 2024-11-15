

with open('shopping_list.txt','r') as sFile:
    count=sum(1 for words in sFile)
    print(count)


with open('data.txt','r') as dFile:
    wordsCount=0
    for line in dFile:
        words=line.split()
        wordsCount+=len(words)
    print(f"The Total words in the data.txt file is : {wordsCount}")