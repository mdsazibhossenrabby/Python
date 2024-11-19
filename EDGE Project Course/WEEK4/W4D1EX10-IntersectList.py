

def getCommonElements(list1,list2):
    return list(set(list1).intersection(list2))

print(f"The Common elements : {getCommonElements([1,2,3,4,5],[2,3,5,6,7,8])}")