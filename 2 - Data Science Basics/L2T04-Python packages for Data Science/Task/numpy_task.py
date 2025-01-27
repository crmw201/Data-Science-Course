import numpy as np

# 1.1) Why doesn't np.array((1,0,0), (0,1,0), (0,0,1,dtype=float)
# create a two-dimensional array?
# The brackets aren't correctly done so it is reading it incorrectly. And
# the data type should be set out apart from the numbers. Also 3 dimensional.
# It should be: 

np.array([(1,0,0), (0,1,0),(0,0,1)], dtype=float)

# 1.2) What is the difference between a = np.array([0,0,0])
# and a = np.array([[0,0,0]])?
# The two sets of square brackets-The second version creates a 2D array 
# with 1 row and 3 columns. Wheras the first one is just a 1D array with 
# 3 elements.

# A 3x4x4 array is created with arr = np.linspace(1,48,48).reshape(3,4,4)
# Index or slice this to obtain:

arr = np.linspace(1, 48, 48).reshape(3, 4,4)


#Looks like: array([[[ 1.,  2.,  3.,  4.],   # Slice 0
 #       [ 5.,  6.,  7.,  8.],
 #       [ 9., 10., 11., 12.],
 #       [13., 14., 15., 16.]],

 #      [[17., 18., 19., 20.],   # Slice 1
 #       [21., 22., 23., 24.],
 #       [25., 26., 27., 28.],
 #       [29., 30., 31., 32.]],

 #      [[33., 34., 35., 36.],   # Slice 2
 #       [37., 38., 39., 40.],
 #       [41., 42., 43., 44.],
 #       [45., 46., 47., 48.]]])

# Much easier to locate when visualised

print(arr[1, 0, 3]) #(second slice, first row, fourth column)  = 20.0
print(arr[0, 2, :]) #(first slice, third row, entire row) = [9. 10. 11. 12.]

# 2D array [[33. 34. 35. 36] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47.48]]
# is the entire of slice 2 so;
print(arr[2, :, :])

# 2D array [[5. 6.], [21. 22.], [37. 38.]] first and second columns from all
# 3 slices so 
print(arr[:, 1, :2])

# 2D array[[36. 35.] [40. 39.] [44. 43.] [48. 47.]] third and 4th column from
# slice 2 but in reverse order 
#arr[2, :, 2:] #selects last two columns in slice 2
#[..., ::-1] # reverses them 
print(arr[2, :, 2:][..., ::-1])

# 2D array [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33]]
# data from all slices, last column of each row, but in reverse order
print(arr[:, ::-1, 0])  # ::- reverses the order of the rows

# 2D array [[1. 4.] [45. 48.]] # have to go manual indexing
# first row, first and last value of slice 0 
# last row, first and last value of slcie 2
print(arr[[0, 2], [0, 3]][:, [0, 3]])# slices, rows, columns

# 2D array [[25. 26. 27. 28], [29. 30. 31. 32.], [33. 34. 35. 36.], 
# [37. 38. 39. 40]]
# Row 2 and 3 from slice 1
# Row 0 and 1 from slice 2
# And all columns
print(arr[1, 2:, :], arr[2, 0:2, :])