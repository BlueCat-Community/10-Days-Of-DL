
# MNIST dataset classification
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

print("Tensorflow version")
print(tf.__version__)



# The number of classes(0~9), features of dataset(28*28)
num_classes = 10
num_features = 784

# learning parameters
learning_rate = 0.01
training_steps = 1000
batch_size = 256
display_step = 50


# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Convert data type to flaot32
X_train, X_test = np.array(X_train, np.float32), np.array(X_test, np.float32)
# Mnist image format data converted to a one-dimensional array
X_train, X_test = X_train.reshape([-1, num_features]), X_test.reshape([-1, num_features])
# data standardization
X_train, X_test = X_train/255., X_test/255.

'''
tf.data.Dataset.from_tensor_slices()
: Creates a Dataset whose elements are slices of the given tensors.

tf.data.Dataset.repeat()
: Repeats this dataset count times.

tf.data.Dataset.batch()
: Combines consecutive elements of this dataset into batches.

tf.data.Dataset.shuffle()
: Randomly shuffles the elements of this dataset.

tf.data.Dataset.prefetch()
: Creates a Dataset that prefetches elements from this dataset.
'''
train_set = tf.data.Dataset.from_tensor_slices( (X_train, y_train) )
train_set = train_set.repeat().shuffle(5000).batch(batch_size).prefetch(1)

# define 'Weight' and 'Bias'
W = tf.Variable(tf.ones([num_features, num_classes]), name="weight")
b = tf.Variable(tf.zeros([num_classes]), name="bias")

def Logistic_Regression(X):
    # Hypothesis formula
    H = tf.matmul(X, W) + b
    
    # Logistic regression
    '''
   You can put the linear revision formula into 
   the softmax function to express the logistic regression.
    '''
    return tf.nn.softmax(H)

'''
tf.one_hot()
: Returns a one-hot tensor.

tf.clip_by_value()
: Clips tensor values to a specified min and max.

tf.reduce_mean()
: Computes the mean of elements across dimensions of a tensor.

'''
def Cross_Entropy(y_pred, y):
    # One hot encoding (categorical data to numerical data)
    y = tf.one_hot(y, depth=num_classes)
    
    y_pred = tf.clip_by_value(y_pred, 1e-9, 1.)
    return tf.reduce_mean(-tf.reduce_sum(y * tf.math.log(y_pred)))

def Accuracy(y_pred, y):
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y, tf.int64))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# Stochastic Gradient Descent (SGD)
optimizer = tf.optimizers.SGD(learning_rate)

'''
tf.GradientTape()
: Record operations for automatic differentiation.

tf.GradientTape().gradient
: Computes the gradient using operations recorded in context of this tape.
'''
def optimization(X, y):
    with tf.GradientTape() as tape:
        pred = Logistic_Regression(X)
        loss = Cross_Entropy(pred, y)

        # get gradient
        gradients = tape.gradient(loss, [W, b])

        optimizer.apply_gradients(zip(gradients, [W, b]))

for step, (batch_X, batch_y) in enumerate(train_set.take(training_steps), 1):
    # Optimization progress with weight and bias updates.
    optimization(batch_X, batch_y)
    
    # Output parameter value whenever step is a multiple of 50.
    if step % display_step == 0:
        pred = Logistic_Regression(batch_X)
        loss = Cross_Entropy(pred, batch_y)
        acc = Accuracy(pred, batch_y)
        print('Step: {}, Loss: {}, Accuracy: {}' .format(step, loss, acc))
        

# Measurement of the accuracy of a trained model.
pred = Logistic_Regression(X_test)
print('Test Accuracy: {}' .format(Accuracy(pred, y_test)))


# ref: https://bioinformaticsandme.tistory.com/156

