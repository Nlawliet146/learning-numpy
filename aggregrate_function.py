import numpy as np

# aggregate functions = these are functions that quickly summarize your data.
# They usually return one final value (like sum, mean, min, max).

array1 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

print(np.sum(array1))
# sum() with only one argument = adds every element in the entire array.
# It basically treats the array like one long list and adds everything inside it.

print(np.mean(array1))
# mean() = gives the average value of all numbers in the array.

print(np.std(array1))
# std() = tells how much the numbers are spread out from the average.

print(np.var(array1))
# var() = variance (this is simply std squared).

print(np.min(array1))
# min() = the smallest number in the whole array.

print(np.max(array1))
# max() = the largest number in the whole array.

print(np.argmin(array1))
# argmin() = gives the index of the smallest value.
# NumPy flattens the array into 1D internally, so the smallest element "1"
# becomes index 0 in that flattened version.

print(np.argmax(array1))
# argmax() = index of the biggest value (same flattening happens here too).

# ------------------------ NOTE ABOUT axis (very important) ------------------------
# axis simply tells NumPy "in which direction do you want to perform the operation?"
# axis = 0 = perform the operation down each column (vertical)
# axis = 1 = perform the operation across each row (horizontal)
# -------------------------------------------------------------------------------

print(np.sum(array1, axis = 0))
# sum() with two arguments = sum(array, axis)
# Here axis = 0 means: add values column by column.
# So it does:
# [1+6, 2+7, 3+8, 4+9, 5+10] = [7, 9, 11, 13, 15]

print(np.sum(array1, axis = 1))
# axis = 1 = add values row by row.
# Row 1 = 1+2+3+4+5 = 15
# Row 2 = 6+7+8+9+10 = 40
# Output = [15, 40]
