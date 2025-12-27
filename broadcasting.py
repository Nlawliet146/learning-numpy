import numpy as np

# broadcasting allows numpy to perform element-wise operations on arrays
# even if their shapes differ; NumPy virtually stretches dimensions of size 1
# without actually copying data in memory

array1 = np.array([[1, 2, 3, 4]])   # shape (1,4)
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])           # shape (4,1)

# array1 has shape (1,4) → one row, four columns
# array2 has shape (4,1) → four rows, one column
# For broadcasting, each dimension must match OR one must be 1.
# Comparing right-to-left:
#   - 4 vs 1 → OK (one is 1)
#   - 1 vs 4 → OK (one is 1)
# So NumPy repeats array1 downward and array2 sideways, forming a (4×4) matrix.

print(array1 * array2)  # element-wise multiplication, result shape = (4,4)

# NOTE: atleast one of the two RULES must be true for all dimension of two arrays