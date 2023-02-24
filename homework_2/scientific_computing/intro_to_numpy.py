import numpy as np

## Exercise 1

x_3d_list = [
  [
    [1, 2, 3], 
    [4, 5, 6]
  ], 
  [
    [10, 20, 30], 
    [40, 50, 60]
  ]
]

x_3d = np.array(x_3d_list)

print(x_3d[1][1][0]) # Should be 40

## Exercise 2

x_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# When dealing with 2D arrays, there isn't a strict relationship with a "row, column" structure, but if we were to assign those to different indexes,
# the first index would likely be the row, and the second index would likely be the column.

## Exercise 3

extract_array = np.array([[5, 6], [50, 60]])

print(extract_array[:, :])

## Exercise 4

multiplication_array = [[5, 6], [50, 60]]
numpy_multiplication_array = np.array([[5, 6], [50, 60]])

print(multiplication_array * 2) # [[5, 6], [50, 60], [5, 6], [50, 60]]
print(numpy_multiplication_array * 2) # [[ 10  12] [100 120]]

# For multiplication by N of a standard list, it simply copies the list onto itself N times. For numpy arrays, it will multiply each value in the data structure
# by N.

## Exercise 5

i = 0.03
M = 100
C = 5

# Define array here
N = np.arange(1, 10)

# price bonds here
bond_prices = [
  ((1 - (1 + i) ** -years) / i) + (M * (1 + i) ** -years)
  for years in N
]

print(bond_prices)