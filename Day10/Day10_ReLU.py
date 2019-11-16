from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import tensorflow as tf


x = tf.random.uniform((3, 3))
y = tf.random.uniform((3, 3))


import timeit
conv_layer = tf.keras.layers.Conv2D(100, 3)

image = tf.zeros([1, 200, 200, 100])

lstm_cell = tf.keras.layers.LSTMCell(10)

@tf.function
def lstm_fn(input, state):
  return lstm_cell(input, state)

input = tf.zeros([10, 10])
state = [tf.zeros([10, 10])] * 2

# warm up
lstm_cell(input, state); lstm_fn(input, state)



class CustomModel(tf.keras.models.Model):

  @tf.function
  def call(self, input_data):
    if tf.reduce_mean(input_data) > 0:
      return input_data
    else:
      return input_data // 2


model = CustomModel()

model(tf.constant([-2, -4]))

@tf.function
def f(x):
  if x > 0:
    # Try setting a breakpoint here!
    # Example:
    #   import pdb
    #   pdb.set_trace()
    x = x + 1
  return x

tf.config.experimental_run_functions_eagerly(True)

# You can now set breakpoints and run the code in a debugger.
f(tf.constant(1))

tf.config.experimental_run_functions_eagerly(False)

def prepare_mnist_features_and_labels(x, y):
  x = tf.cast(x, tf.float32) / 255.0
  y = tf.cast(y, tf.int64)
  return x, y

def mnist():
  (x, y), _ = tf.keras.datasets.mnist.load_data()
  ds = tf.data.Dataset.from_tensor_slices((x, y))
  ds = ds.map(prepare_mnist_features_and_labels)
  ds = ds.take(20000).shuffle(20000).batch(100)
  return ds

train_dataset = mnist()

model = tf.keras.Sequential((
    tf.keras.layers.Reshape(target_shape=(28 * 28,), input_shape=(28, 28)),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(10)))
model.build()
optimizer = tf.keras.optimizers.Adam()

compute_loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

compute_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()


def train_one_step(model, optimizer, x, y):
  with tf.GradientTape() as tape:
    logits = model(x)
    loss = compute_loss(y, logits)

  grads = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(grads, model.trainable_variables))

  compute_accuracy(y, logits)
  return loss


@tf.function
def train(model, optimizer):
  train_ds = mnist()
  step = 0
  loss = 0.0
  accuracy = 0.0

  for x, y in train_ds:
    step += 1
    loss = train_one_step(model, optimizer, x, y)
    if step % 10 == 0:
      tf.print('Step', step, ': loss', loss, '; accuracy', compute_accuracy.result())
  return step, loss, accuracy


step, loss, accuracy = train(model, optimizer)
print('Final step', step, ': loss', loss, '; accuracy', compute_accuracy.result())

