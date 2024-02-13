# numpy basic operations
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr, type(arr))

# ---------------------------------------
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)   # ndim is the function to get the dimension of the array
print(b.ndim)   # in numpy , we call array as ndarray
print(c.ndim)
print(d.ndim)
# ----------------------------------------
arr = np.array([1, 2, 3, 4])

print(arr.dtype) # dtype is the function to get the data type of data present in the array.
#------------------