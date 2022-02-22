import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view()
arr[0] = 42
x[1] = 54

print(arr)
print(x)
