

from functools import reduce

numbers=[i for i in range(1,11)]

sum=reduce(lambda x,y: x+y,numbers)

print(f"Sum of the list (1 to 10) numbers are : {sum}")