import numpy as np

# Scalar Arthmetic , scalar mean single value, basically linear algebra

array = np.array([1, 2, 3])

print(array * 2)
print(array + 2)
print(array - 2)
print(array / 2)
print(array ** 2)

# Vectorized math funcs

array = np.array([1.01, 2.9, 3.4])

print(np.sqrt(array)) # sqrt is an built in math function in numpy
print(np.round(array)) # rounded
print(np.floor(array)) # round down
print(np.ceil(array)) # round up

print(np.pi) # built in constant

# EXERCISE

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)

# ELEMENT-WISE ARITHMETIC

array1 = np.array([4, 5, 6])
array2 = np.array([7, 8, 9])

# we can use arithmetic on each element separately of two arrays
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# COMPARISION

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores >= 60) # will return boolean array, true only if condtion satisfy

scores[scores == 100] = 0 # now the element which satisfy this conditoin, will convert into 0
print(scores)