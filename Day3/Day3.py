# # Tensorflow 2.0 - Linear regression

import tensorflow as tf
print(tf.__version__)


# # Create Data
# 
# Before creating a simple linear regression,
# We need to data.
# 
# In this code, we generate ramdom data using the below code.
# 
# **Data Information**
# - Number of data: 1000
# - Y = 0.1X + 0.3 + noise(half of x's range)

import numpy as np
num_points = 1000
vectors_set = []
for i in range(num_points):
    x= np.random.normal(0.0, 0.55)
    y= x * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x, y])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]


# ## Check This Data

import matplotlib.pyplot as plt

plt.plot(x_data, y_data, 'ro', label='Original data')
plt.show()


# # Set Hypothesis for machine learning
# 
# We want linear regression. And linear regression expressed
# <code>H = Wx + b</code>
# 
# So You must set to W, b and Hypothesis.


# if you want set 0 to value, use tf.zeros.
# Usually these variables are initialized randomly. 
W = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

@tf.function
def forward(x):
    return W * x + b

print("W :", W)
print("b :", b)


# Define Loss and Gradient Function
# We need to define loss function for gradient and performance measurement.
# Next, We need to create graident_descent function.
# It performs differential about W, b using loss for global optimization.

def loss(predicted_y, desired_y):
    # [(SUM of all element ((predicted_y - y)^2)] / n
    return tf.reduce_mean(tf.square(predicted_y - desired_y))

def gradient_descent(inputs, outputs, learning_rate):
    # GradientTape is record all computed process. -> It is used to gradient.
    with tf.GradientTape() as t:
        current_loss = loss(forward(inputs), outputs)
    dW, db = t.gradient(current_loss, [W, b])
    W.assign_sub(learning_rate * dW)
    b.assign_sub(learning_rate * db)


# Train model (3 times only)
# Check that the loss value is decreased and changed H(Hypothesis)

import matplotlib.pyplot as plt
def display_graph():
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, W * x_data + b)
    plt.show()

for i in range(3):
    gradient_descent(x_data, y_data, 0.5)
    print("Loss", loss(forward(x_data), y_data).numpy())
    display_graph()


# More...

for i in range(30):
    gradient_descent(x_data, y_data, 0.5)
    print("i={0}, loss = {1}".format(i,loss(forward(x_data), y_data).numpy()))
display_graph()


# Check Result

print("Y = {0:.3}X + {1:.3}".format(W[0].numpy(), b[0].numpy()))
print("Loss = {0}".format(loss(forward(x_data), y_data).numpy()))


# ### Reference
# - https://tensorflow.blog/2-%ED%85%90%EC%84%9C%ED%94%8C%EB%A1%9C%EC%9A%B0-%EC%84%A0%ED%98%95-%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D-first-contact-with-tensorflow/
# - https://www.tensorflow.org/tutorials/customization/custom_training
# - https://tensorflow.org/guide/migration_guide?hl=ko
# - https://www.tensorflow.org/tutorials/customization/autodiff?hl=ko



