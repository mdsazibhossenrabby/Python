"""
it dose not create new variable when reassigned value in existing variable

-normal variables
-list
-dictionaries
-sets
"""

#list
numbers=[1,1,2,3,4]
firstLocation=id(numbers) # id() fuction return variable address
print(f"The list is : {numbers} \nfirst item address is : {firstLocation}")

ZeroIndex1=id(numbers[0])
print(ZeroIndex1)

numbers[0]=0
mFirstLocation=id(numbers)
print(f"The reasigned list is : {numbers} \nfirst item address after reasigned is : {mFirstLocation}")

ZeroIndex2=id(numbers[0])
print(ZeroIndex2)

"""
Here ZeroIndex1 and ZeroIndex2 are different because id() function
does not returns exact memory address it returns unique identifier of indidul objects.
since 
"""