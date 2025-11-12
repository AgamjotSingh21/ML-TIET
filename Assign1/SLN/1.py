import numpy as np

# 1(a) 
arr = np.array([1, 2, 3, 6, 4, 5])
reversed = arr[::-1]
print(" Reversed array:", reversed)

#(b) 
array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
flattened1 = array1.flatten()
flattened2 = array1.ravel()
print("Flattened array (method 1):", flattened1)
print("Flattened array (method 2):", flattened2)

#(c) 
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
comparison = np.array_equal(arr1, arr2)
print("Are the arrays equal?", comparison)

#(d)
x = np.array([1,2,3,4,5,1,2,1,1,1])
count_x = np.bincount(x)
most_frequent_x = np.argmax(count_x)
indices_x = np.where(x == most_frequent_x)
print("\n(d) i. Most frequent value in x:", most_frequent_x)
print("\n(d) i. Indices of most frequent value in x:", indices_x)
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
count_y = np.bincount(y)
most_frequent_y = np.argmax(count_y)
indices_y = np.where(y == most_frequent_y)
print("\n(d) ii. Most frequent value in y:", most_frequent_y)
print("\n(d) ii. Indices of most frequent value in y:", indices_y)

#(e) 
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum_all = np.sum(gfg)
sum_row_wise = np.sum(gfg, axis=1)
sum_column_wise = np.sum(gfg, axis=0)
print("\n(e) i. Sum of all elements:", sum_all)
print("\n(e) ii. Sum of all elements row-wise:", sum_row_wise)
print("\n(e) iii. Sum of all elements column-wise:", sum_column_wise)

#(f) 
n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
sum_diagonal = np.trace(n_array)
eigenvalues, eigenvectors = np.linalg.eig(n_array)
inverse_matrix = np.linalg.inv(n_array)
determinant = np.linalg.det(n_array)
print("\n(f) i. Sum of diagonal elements:", sum_diagonal)
print("\n(f) ii. Eigen values of matrix:", eigenvalues)
print("\n(f) iii. Eigen vectors of matrix:", eigenvectors)
print("\n(f) iv. Inverse of matrix:\n", inverse_matrix)
print("\n(f) v. Determinant of matrix:", determinant)

#(g) i
p_i = np.array([[1, 2], [2, 3]])
q_i = np.array([[4, 5], [6, 7]])
multiplic_i = np.dot(p_i, q_i)
cov_i = np.cov(p_i, q_i)
print("\n(g) i. Multiplication of matrices:\n", multiplic_i)
print("\n(g) i. Covariance between matrices:\n", cov_i)

# ii
p_ii = np.array([[1, 2], [2, 3], [4, 5]])
q_ii = np.array([[4, 5, 1], [6, 7, 2]])
multiplic_ii = np.dot(p_ii, q_ii)
print("\n(g) ii. Multiplication of matrices:\n", multiplic_ii)

#(h)
x_h = np.array([[2, 3, 4], [3, 2, 9]])
y_h = np.array([[1, 5, 0], [5, 10, 3]])

inner_product = np.dot(x_h, y_h.T)
outer_product = np.outer(x_h.flatten(), y_h.flatten())
cartesian_product = np.array(np.meshgrid(x_h.flatten(), y_h.flatten())).T.reshape(-1, 2)

print("\n(h) Inner product:\n", inner_product)
print("\n(h) Outer product:\n", outer_product)
print("\n(h) Cartesian product:\n", cartesian_product)




# Q2 (a)
array = np.array([[1, -2, 3],[-4, 5, -6]])
abs_array = np.abs(array)
print("\n\n(a) Element-wise absolute value:\n", abs_array)

# (b) 
flattened_array = array.flatten()
percentiles_flattened = np.percentile(flattened_array, [25, 50, 75])
percentiles_column = np.percentile(array, [25, 50, 75], axis=0)
percentiles_row = np.percentile(array, [25, 50, 75], axis=1)

print("\n(b) Percentiles of flattened array (25th, 50th, 75th):", percentiles_flattened)
print("\n(b) Percentiles of each column (25th, 50th, 75th):\n", percentiles_column)
print("\n(b) Percentiles of each row (25th, 50th, 75th):\n", percentiles_row)

# (c) 
mean_flattened = np.mean(flattened_array)
median_flattened = np.median(flattened_array)
std_flattened = np.std(flattened_array)

mean_column = np.mean(array, axis=0)
median_column = np.median(array, axis=0)
std_column = np.std(array, axis=0)

mean_row = np.mean(array, axis=1)
median_row = np.median(array, axis=1)
std_row = np.std(array, axis=1)

print("\n(c) Mean of flattened array:", mean_flattened)
print("\n(c) Median of flattened array:", median_flattened)
print("\n(c) Standard Deviation of flattened array:", std_flattened)

print("\n(c) Mean of each column:", mean_column)
print("\n(c) Median of each column:", median_column)
print("\n(c) Standard Deviation of each column:", std_column)

print("\n(c) Mean of each row:", mean_row)
print("\n(c) Median of each row:", median_row)
print("\n(c) Standard Deviation of each row:", std_row)

# (d) 
a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
floor_a = np.floor(a)
ceiling_a = np.ceil(a)
truncated_a = np.trunc(a)
rounded_a = np.round(a)

print("\n(d) Original array:", a)
print("\n(d) Floor values:", floor_a)
print("\n(d) Ceiling values:", ceiling_a)
print("\n(d) Truncated values:", truncated_a)
print("\n(d) Rounded values:", rounded_a)



# Q3: 
array = np.array([10, 52, 62, 16, 16, 54, 453])

# i. 
sorted_array = np.sort(array)
print("\n(a) i. Sorted array:", sorted_array)

# ii. 
indices_sorted_array = np.argsort(array)
print("\n(a) ii. Indices of sorted array:", indices_sorted_array)

# iii. 
smallest_elements = np.partition(array, 4)[:4]
print("\n(a) iii. 4 smallest elements:", smallest_elements)

# iv. 
largest_elements = np.partition(array, -5)[-5:]
print("\n(a) iv. 5 largest elements:", largest_elements)

# (b) 
array_b = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. 
integer_elements = array_b[np.mod(array_b, 1) == 0]
print("\n(b) i. Integer elements only:", integer_elements)

# ii. 
float_elements = array_b[np.mod(array_b, 1) != 0]
print("\n(b) ii. Float elements only:", float_elements)