

import numpy as np

array1=np.array([1,2])
array2=np.array([3,4])

stackedArr=np.vstack((array1,array2))
print(stackedArr)

stackedArr=np.hstack((array1,array2))
print(stackedArr)