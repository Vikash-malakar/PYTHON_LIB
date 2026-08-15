import numpy as np

arr = np.array([10, 20, np.nan, 40, 50])

print("NaN:", np.isnan(arr))

clean_data = arr[~np.isnan(arr)]

print(clean_data)
