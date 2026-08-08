import numpy as np

arr = np.array([10, 20, 30, 40])

new_arr = np.insert(arr, 2, 99)
print(new_arr)

new_arr = np.delete(arr, 1)
print(new_arr)