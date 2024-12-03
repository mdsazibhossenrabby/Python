

import numpy as np


# 0 to n-1
print("0 to n-1")
arr = np.arange(10)
print(arr)

# n to m-1
print("n to m-1")
arr1 = np.arange(5, 15)
print(arr1)

# n to m-1 with step size x
print("n to m-1 with step size x")
arr2 = np.arange(0, 10, 2)
print(arr2)

# m to n-1  with step size -x
print("m to n-1  with step size -x")
arr3 = np.arange(20, 0, -3)
print(arr3)

# floating point 
print("floating point")
arr4 = np.arange(0.0, 5.0)
print(arr4)

arr5 = np.arange(0.0, 4.0,0.3)
print(arr5)

# Specify Data Type

arr6 = np.arange(0.0, 5.0, 0.5, dtype=int)
print(arr6)

arr61 = np.arange(0, 5, 0.5).astype(int)
print(arr61)

arr7 = np.arange(0, 10, 2, dtype=int)
print(arr7)

# Empty Array 

arr8 = np.arange(10, 5) #start> end
print(arr8)

