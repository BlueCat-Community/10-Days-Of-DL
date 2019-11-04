import tensorflow as tf
import numpy as np


# ## 1. Array and Slicing
# ### Axis: selected by row/column(axis=0:column, axis=1:row)

arr=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)

#rank:number of dimensions of array
print(arr.ndim)

#shape
print(arr.shape)# 3 x 3

#slicing array
print(arr[2:4])# 6,7,8
print(arr[:2])# 


# ## 2. Matmul, Multiply-

matrix1=tf.constant([[1,2],[3,4]])
matrix2=tf.constant([[1],[2]])

#Matmul: multiply of matrix1 and matrix2
print("Matmul:")
print(tf.matmul(matrix1, matrix2).numpy())


#Multiply: 
print("Multiply:")
print((matrix1 * matrix2).numpy())#this output came out because of broadcasting


# ## 3. Broadcasting
# :make calculation of different-shaped matrix available

mat1=tf.constant([[1,2]])
mat2=tf.constant([[3,4]])
print("Multiply:")#when mat1,mat2 is same shape
print((mat1+mat2).numpy())

mat1=tf.constant([[1,2]])
mat2=tf.constant([[3]]) 
print("Broadcasting:")#when mat1,mat2 has different shape
print((mat1+mat2).numpy())#broadcasting use [3,3] shape to calculate


# ## 4-1.Reduce Mean
# :return mean of matrix selected by axis

x=tf.constant([[1.,2.],[3.,4.]])

#reduce_mean(): return minimum values of each axis
print(tf.reduce_mean(x,axis=0).numpy())#output:[mean(1,3),mean(2,4)]
print(tf.reduce_mean(x,axis=1).numpy())#output:[mean(1,2),mean(3,4)]
print(tf.reduce_mean(x).numpy())#if axis is not entered, return just mean(x)


# ## 4-2.Reduce Sum
# :return sum of matrix selected by axis

print(tf.reduce_sum(x , axis=0).numpy())
print(tf.reduce_sum(x , axis=1).numpy()) 
print(tf.reduce_sum(x , axis=-1).numpy()) # same axis = 1


# ## 5.Argmax
# :return position of maximum value by axis

x=[[0,1,2],[2,1,0]]

print(tf.argmax(x,axis=0).numpy()) #position of (2,1,2)
print(tf.argmax(x,axis=1).numpy()) #position of (2,2)
print(tf.argmax(x,axis=-1).numpy()) #same as axis=1


# ## 6.Reshape(reshape,squeeze,expand)
# :return reshaped array of input matrix

x = tf.constant([[[0, 1, 2],
                  [3, 4, 5]],
                 [[6,7,8],
                  [9,10,11]]
                ])
print(x.shape) #2*(2*3)

print("Reshape:")
print(tf.reshape(x,shape=[-1,3]).numpy()) 

#If you want more, try these
#print(x.numpy()) #result expired after reshape function call
#print(tf.reshape(x,shape=[-1,1,3]).numpy()) #add 1 more rank 

print("Squeeze:") #simplify the unused rank
print(tf.squeeze([[[0],[1],[2]]]).numpy())

print("\nExpand_dims:") #expand dimension of matrix
print(tf.expand_dims([0,1,2], 1).numpy())


# ## 7.One-Hot
# : express numbers by one-hot encoding.
# #### ex) [0,1,2,3] will be same as below.
# 0 -> [1,0,0,0]<br>
# 1 -> [0,1,0,0]<br>
# 2-> [0,0,1,0]<br>
# 3 -> [0,0,0,1]<br>
# 0 -> [1,0,0,0]<br>

print("example:")
arr = [0, 1, 2, 3]
print(tf.one_hot(arr, depth=4).numpy())


# ## 8.Type-casting
# :type casting array

arr = [1.8, 2.2, 4.1, 0.5] 
print(tf.cast(arr,tf.int32).numpy()) #type-casting float array to int32
print(tf.cast([True,False,1==1,0==1],tf.int32).numpy()) #casting boolean to int32


# ## 9.Stack
# : return stack of input arrays by directed by axis

x = [1, 4]
y = [2, 5]
z = [3, 6]

print("Stack_axis0:") #axis 0: stacked in a row
print(tf.stack([x,y,z],axis=0).numpy()) #axis=0
print("Stack_axis1:") #axis 1: stacked in a column
print(tf.stack([x,y,z],axis=1).numpy()) #axis=1


# ## 10.Ones,Zeros
# : return new arrays initialized with 1(ones) or 0(zeros)

print("Ones:")
print(tf.ones([2,3]).numpy()) #create new array of ones in size(2*3)
print("Zeros:")
print(tf.zeros([3,4]).numpy()) #create new array of zeros in size(3*4)


# ## 11.Zip
# :return 2 arrays binded by index

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print("zip(a,b):")
for x,y in zip(a,b):
    print(x,y)
print("zip(a,b,c):")
for x,y,z in zip(a,b,c):
    print(x,y,z)