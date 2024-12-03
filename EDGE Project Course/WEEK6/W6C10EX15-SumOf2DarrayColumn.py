
import numpy as np

array2D=np.array([[1,2],[3,4],[5,6]])
colSum=np.sum(array2D,axis=0)
print(colSum)

RowSum=np.sum(array2D,axis=1)
print(RowSum)