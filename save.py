import numpy as np

# Save an Array

array1 = np.array([[1, 2, 3], 
                   [4, 5, 6]])

np.save("data", array1) # data is the name of file in which array is stored (format is .npy)

print("NUmpy array was saved, this msg is just to check that the code till now was okay")

# we can save it anywhere by giving relative or preferably absolute location of the folder 
# in np.save(file_name, array_name) in the file_name, for example:
# np.save("C:\\Users\\joker\\OneDrive\\Desktop\\data", array1)
# \\ means literal \ character, whereas \ is used for function like \n which means newline chracter
# you can also use / for location


# To save multiple numpy array
array2 = np.array([[1, 2, 3], 
                   [4, 5, 6]])
array3 = np.array([1.1, 1.2, 1.7, 1.9])

np.savez("data_multiple", array2, array3) # z means zipt, used for multiple array, each array is passed as an additoinal argument
print("check message")

# we can save data in compressed manner, used when using huge data

np.savez_compressed("data_compressed", array2, array3)
print("check message")