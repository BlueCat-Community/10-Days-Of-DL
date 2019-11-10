import numpy as np
import tensorflow as tf
tf.__version__

# dataset (numpy)
input_data = np.array([[0,0], [0,1],[1,0],[1,1]]).astype(np.float)
output_data = np.array([[0], [1], [1], [0]]).astype(np.float)

# datset (tf)
train_dataset = tf.data.Dataset.from_tensor_slices((input_data, output_data))
test_dataset = tf.data.Dataset.from_tensor_slices((input_data, output_data))

# parameters for dataset
BATCH_SIZE = 1
SHUFFLE_BUFFER_SIZE = 4

# redefine dataset
train_dataset = train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
])

# optimizer, loss function
sgd = tf.keras.optimizers.SGD(lr=0.01, decay=0, momentum=0.99, nesterov=True)
model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])

# fit
model.fit(train_dataset, epochs=500, verbose=False)
print('Finished training the model')

# predict
print(model.predict(test_dataset))

# result (accuracy)
test_loss, test_acc = model.evaluate(test_dataset)
print('Accuracy:', test_acc)


######################################################################
# keras model subclassing - same task

class MyLayer(tf.keras.layers.Layer):
    def __init__(self, name="MyLayer", **kwargs):
        super(MyLayer, self).__init__(name=name, **kwargs)
        self.l1 = tf.keras.layers.Dense(16, activation=tf.nn.sigmoid, input_dim=2)
        self.l2 = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
    def call(self, x):
        x = self.l1(x)
        x = self.l2(x) # put output of above layer
        return x

class MyModel(tf.keras.Model):
    def __init__(self, name="MyModel", **kwargs):
        super(MyModel, self).__init__(name=name, **kwargs)
        self.my_layer = MyLayer()
    def call(self, inputs):
        return self.my_layer(inputs)
    
model = MyModel()

sgd = tf.keras.optimizers.SGD(lr=0.01, decay=0, momentum=0.99, nesterov=True)

model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])
model.fit(train_dataset, epochs=500)

# result (accuracy)
test_loss, test_acc = model.evaluate(test_dataset)
print('Accuracy:', test_acc)

