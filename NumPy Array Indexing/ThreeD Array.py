import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 1])
print(arr[0, 1, 2])
print(arr[1, 0, 2] + arr[1, 1, 1])
print(arr[0, 1, 1] + arr[1, 1, 0])

print("Negative Indexing")
print(arr[-1, -2, -2])
print(arr[-2, -1, -1])
print(arr[-1, -2, -1] + arr[-1, -1, -2])
print(arr[-2, -1, -2] + arr[-1, -1, -3])
