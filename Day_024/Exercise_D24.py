# We are told to repeat all the exercise in this day

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1
print('numpy:', np.__version__)
print(dir(np))

# 2
python_list = [1,2,3,4,5]
print('Type:', type (python_list)) 
print(python_list) 

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))
print(numpy_array_from_list)

# 3
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# 4
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# 5
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) 
print('python_tuple: ', python_tuple) 

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) 
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

# 6
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],[4,5,6,7],[8,9,10, 11]])
print(three_by_four_array.shape)

# 7
# Checking numpy array data type
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# 8
# Getting the size of numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
print('The size:', numpy_array_from_list.size) 
print('The size:', two_dimensional_list.size) 

# 9
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# 10
# Getting rows from 2 dimensional array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

# 11
# Getting column from 2 dimensional array
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

# 12 
# How to represent a missing value
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# 13
# Getting random numbers
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

# 14
# Numpy functional
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
print('sd: ', two_dimension_array.std())

# 15
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

# 16
np_normal_dis = np.random.normal(5, 0.5, 1000)
np_normal_dis
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

# 17 
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# 18
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()