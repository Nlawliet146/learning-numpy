import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# access our array using subscript operator which is this bracket []
# array[start:end:step] #step = 1, by default

print(array[0:2]) # ending here is 2, which is exclusive, that is the slicing will not include the index of end 
print(array[0:4:2])

print(array[::2]) # start and end are not given, therefor it will includ all rows by default

print(array[::-1]) # will print in reverse

print(array[:, 0]) # before the comma it is indexing of outernmost list, after coma it is inner. : means all index, so this will give us an array  consisting first index of each inner array
print(array[:, -1])