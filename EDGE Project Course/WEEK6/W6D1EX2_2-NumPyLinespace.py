

import numpy as np

# by default divide into 50 (num=50)
arr1 = np.linspace(0, 10)
print(arr1)


arr2 = np.linspace(0, 10,num=5)
print(arr2)

#Excluding the Endpoint
arr3 = np.linspace(0, 10,num=5, endpoint=False)
print(arr3)

#Negative 
arr4 = np.linspace(-10, 0, num=5)
print(arr4)

#Negative but integer
arr4 = np.linspace(-10, 0, num=5,dtype=int)
print(arr4)



"""
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

start: The starting value of the sequence.
stop: The end value of the sequence.
num (optional): The number of samples to generate (default is 50).
endpoint (optional): If True, stop is included as the last value (default is True).
retstep (optional): If True, return the step size between values (default is False).
dtype (optional): The data type of the output array.
axis (optional): The axis in the result along which the values are stored. Default is 0.
    
"""