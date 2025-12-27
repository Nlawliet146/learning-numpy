import numpy as np

# filtering = refers to the process of selecting elements from an array that matches a given condition

ages = np.array([[21, 17, 65, 20, 19, 16, 30, 18],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18] # syntax: array[condition] for filtering 
# this boolean indexing, this will flatten the array
print(teenagers)

adults = ages[(ages >= 18 ) & (ages < 65)] # in normal python the logical operator of and is simply and
                                          # but since numpy is extension of c++ we will use & for and
print(adults)

senior = ages[ages >= 65]
print(senior)

evens = ages[ages % 2 == 0]
print(evens)

odds = ages[ages % 2 != 0]
print(odds)

# if you want to filter but without flattening the array and retaining orignal shape:

adults2 = np.where((ages >= 18) & (ages < 65), ages, 0) # syntax: np.where(conditions, array_name, fill value)
                                     # fill value: since we are filtering while keeping the orignal shape
                                     # we need to give a default value which will be applied when while 
                                     # iterarting we find an element outside of our conditions set
                                     # usually people use 0, -1 or np.nan (not a number)
print(adults2)
        