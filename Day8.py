import tensorflow as tf
import numpy as np
import pprint

# 1D Array
t = np.array([0., 1., 2., 3., 4., 5., 6.])

print(t)

# Indexing array
print(t[-1]) # array t's last index

# Slicing array
print(t[:3]) # array t's #0~2
print(t[:-1]) # array t's #2~last-1

# 2D Array

pp = pprint.PrettyPrinter(indent=4)
 
t2 = np.array([[0., 1., 2.],[3., 4., 5.],[6., 7., 8.],[9., 10., 11.],[12., 13., 14.]])

pp.pprint(t2)

print(t2.ndim) # check t2' rank
print(t2.shape, end = "\n\n") # check t2's shape

# Indexing array
print(t2[1 ,2])

# Slicing array
print(t2[:,2]) # Column 2's all index
print(t2[0,:]) # Row 0's all index


# Matmul vs Multiply

matrix1 = tf.constant([[1, 2],[3, 4]])
matrix2 = tf.constant([[1],[2]])

print('Matrix1  shape:', matrix1.shape)
print('Matrix2  shape:', matrix2.shape, end = "\n\n")

# Matmul arrays
print("Matmul example")
print(tf.matmul(matrix1, matrix2).numpy(), end="\n\n")

# Multiply arrays
print("Multiply example")
print((matrix1 * matrix2).numpy())


# Broadcasting

# When shape is correct
matrix1 = tf.constant([3, 3])
matrix2 = tf.constant([3, 3])
print((matrix1 + matrix2).numpy(), end="\n\n")

# When shape is different - automatically broadcasting
matrix1 = tf.constant([3, 6])
matrix2 = tf.constant([10])
print((matrix1 + matrix2).numpy(), end="\n\n")


# Reduce mean and Reduce sum

# Reduce mean
print("Reduce mean")

# When using int type
print(tf.reduce_mean([1, 2], axis =0).numpy())

# When using float type
x = [[1., 2.],[3., 4.,]]
print(tf.reduce_mean(x).numpy(), end="\n\n")

# Reduce sum
print("Reduce sum")

# array x's sum
print(tf.reduce_sum(x).numpy())
# array axis -1's sum and mean
print(tf.reduce_mean(tf.reduce_sum(x, axis = -1)).numpy())


# Argmax

x = [[0, 1, 2],
    [2, 1, 0]]

# axis 0's max value's index
print(tf.argmax(x, axis = 0).numpy())

# axis -1's max value's index
print(tf.argmax(x, axis = -1).numpy())


# Reshape

t = np.array([[[0, 1, 2],
              [3, 4, 5]],
             [[6, 7, 8],
             [9, 10, 11]]])

# t's shape
print(t.shape, end = "\n\n")

# reshape array t
print(tf.reshape(t, shape = [-1, 3]).numpy(), end = "\n\n")

# reshape array t
print(tf.reshape(t, shape = [-1,1, 3]).numpy(), end = "\n\n")

# squeeze
print(tf.squeeze([[0], [1], [2]]).numpy(), end = "\n\n")

# expand
print(tf.expand_dims([0 ,1 ,2], 1).numpy())


# One-hot
print(tf.one_hot([[0], [1],[2]], depth = 3).numpy())

t = tf.one_hot([[0], [1], [2], [0]], depth = 3).numpy()
print(tf.reshape(t, shape = [-1, 3]).numpy())

# Casting

# Change float to int
tf.cast([1.8, 2.2, 3.3, 4.9], tf.int32).numpy()

# Change boolean to int
tf.cast([True, False, 1 == 1, 0 == 1], tf.int32).numpy()



# Stack

x = [1, 4]
y = [2, 5]
z = [3, 6]

# Stack three arrays
tf.stack([x, y, z]).numpy()

# Stack three arrays and axis is 1
tf.stack([x, y, z], axis = 1).numpy()

# Stack three arrays and axis is 0
tf.stack([x, y, z], axis = 0).numpy()



# Ones and Zeros like

x = [[2, 1, 0],
    [0, 1, 2]]

# fill array with 1
tf.ones_like(x).numpy()

# fill array with 0
tf.zeros_like(x).numpy()


# Zip

for x, y in zip([1,2,3], [4,5,6]):
    print(x, y)
    
print()
    
for x, y, z in zip([1, 2, 3], [4, 5, 6], [7, 8, 9]):
    print(x, y, z)
