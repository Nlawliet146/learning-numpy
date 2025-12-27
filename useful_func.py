import numpy as np

array = np.zeros(10) # zeros function return an array according to given argument
                     # 10 as an argument will give 1D array with 10 elemnts filled with zero
print(array)

array = np.zeros((2, 10)) # now it will give a 2D array with 2 outer list each with 10 zeros
print(array)

array = np.zeros((2, 3, 10)) # now it will give a 3D array with 2 outer list each with 3 inner list with 10 zeros as element
print(array)

# similarly we have for 1
array = np.ones((2,10))
print(array)

# for an custom value
array = np.full((2, 10), 'A')
print(array)

# eye() gives an identity matrix of 2D
array = np.eye(3) # 2 means two rows and two coloums
print(array)

# empty
array = np.empty((2,3)) # gives some random numbers according to size and shape of array
print(array)

# arange
array = np.arange(1, 100, 2) # we pass in three arguments: start, end(one step behind the ending given), step(default value 1)
print(array)

# linespace
array = np.linspace(0, 10, 4) # start, stop, num
# linspace() creates an array between start and stop with a specific number of evenly spaced values
# Unlike arange(), the stop value IS included, and the third argument controls how many values to generate

print(array)