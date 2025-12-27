import numpy as np

# Load a Numpy array

array = np.load("data.npy")

print(array) # shape is retained

# loading multiple array name

arrays = np.load("data_multiple.npz")
print(arrays) # output is: NpzFile 'data_multiple.npz' with keys: arr_0, arr_1, we can use these keys to access the array

array1 = arrays["arr_1"] # or arr_0
print(array1)