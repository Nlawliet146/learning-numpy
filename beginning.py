# numpy short for numerical python, basically disguised c++ which makes the code fast!
 
import numpy as np # we are using np as alias

# print(np.__version__) to check the version

my_list = [1, 2, 3, 4]
print(my_list * 2) #multiplying y 2 will give the list but twice

array1 = np. array([1, 2, 3, 4]) #this here is numpy list
print(array1)
print(array1 * 2) # as we can see multiplying a numpy array by 2, will not double the list itself but will double the value..

array2 = np.array('A') # this is a zero dimension array, cuz well it has no list in it
print(array2.ndim) # ndim means n dimension, this is an attribute which gives dimension of array

array3 = np.array([1, 2, 3, 4]) # this is a single dimension array, cuz it has 1 list, 
print(array3.ndim)

array4 = np.array([[1, 2],
                   [3, 4],
                   [5, 6]]) # this is a 2 dimension, cuz well it is list inside list, so 2. Also called matrix
# VERY IMPORTANT = The list inside list shall have SAME NUMBER OF ELEMENTs, that is here in the 'inside' list there are two elements namely 1 and 2, so all other list shall only have two element
print(array4.ndim)

print(array4.shape) # answer is (3,2) that means 3 'rows' and 2 'coloumn'

array5 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
# the first 3 in (3,3,3) represent that the 'outermost' list have 3 elements, likewise the secondary list also have 3 elements, while the innermost list also have 3 elements
print(array5.shape)

#to print elements we will use the same logic that is, the first input always refer to outermost list
print(array5[0][0][0]) # this means print the 0 index of outer list, in that print 0 index of second list, in that print 0 index of inner list
print(array5[0][1][2])

# this refer to chain indexing, in numpy it is called multidimensional indexing

name = array5[1][1][1] + array5[0][0][0] + array5[1][1][0] + array5[0][0][0] + array5[1][1][1]
print(name)