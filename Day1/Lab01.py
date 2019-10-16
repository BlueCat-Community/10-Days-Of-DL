#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


"""
Lab1 basic 
change existing lab1 code to tensorflow version 2
existing code ; node1+node2
"""

#make constant
node1= tf.constant(3)
node2=tf.constant(4)

node3=node1+node2

print(node3)

@tf.function # session 대신 사용
def add(x,y):
    return x+y

print(add(tf.Variable(3),node2))

