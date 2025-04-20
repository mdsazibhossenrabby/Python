alists=["Apple",50,3.1416,True,'C',"SAZIB"]
print(alists)

# add item at last
alists.append("Hossen")
print(alists)

#insert at any index
alists.insert(1,False)
print(alists)

# remove and return valu at index
print(alists.pop(1))
print(alists)
#remove value from list by value
print(alists.remove("SAZIB"))
print(alists)


# sort the list 
numbers=[2,5,1,9,3,4,6,4]
numbers.sort()
print(numbers)

# reverse the number lits 
numbers.reverse()
print(numbers)

#count any element
print(numbers.count(4))

#Find index of any element
print(alists.index(True))