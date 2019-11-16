import tensorflow as tf
from tensorflow import keras

print(tf.__version__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mnist = keras.datasets.fashion_mnist

type(mnist)

(X_train, y_train),(X_test, y_test) = mnist.load_data()

print(X_train.shape, y_train.shape)

print(np.max(X_train))
print(np.mean(X_train))
print(y_train)


class_names = ['top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

#Data Exploation
print(X_train.shape)
print(X_test.shape)


plt.figure()
plt.imshow(X_train[1])
plt.colorbar()
plt.show()

print(y_train)

X_train = X_train/255.0
X_test = X_test/255.0

plt.figure()
plt.imshow(X_train[1])
plt.colorbar()
plt.show()

# Build the model with TF 2.0
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

model = Sequential()
model.add(Flatten(input_shape = (28,28)))
model.add(Dense(120, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.summary()

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, y_train, epochs =10)

test_loss, test_acc = model.evaluate(X_test, y_test)
print('test accuracy = ', test_acc)

from sklearn.metrics import accuracy_score

y_pred=model.predict_classes(X_test)
print('accuracy score = ', accuracy_score(y_test, y_pred))

print(y_pred)

pred = model.predict(X_test)

print('np.argmax(pred[0]) = ', np.argmax(pred[0]))
print('np.argmax(pred[1]) = ', np.argmax(pred[1]))

# reference >> https://www.youtube.com/watch?v=nVvhkVLh60o
