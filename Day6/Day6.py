from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf


def loss(model, x, y):
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    y_ = model(x)
    return loss_object(y_true=y, y_pred=y_)


def pack_features_vector(features, labels):
    # come together characteristics into one array
    features = tf.stack(list(features.values()), axis=1)
    return features, labels


def grad(model, inputs, targets):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, targets)
    return loss_value, tape.gradient(loss_value, model.trainable_variables)


def SoftMax():
    print("Version Of tensorflow: {}".format(tf.__version__))
    train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

    train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                               origin=train_dataset_url)

    print("Dataset copy place: {}".format(train_dataset_fp))

    # Column order
    column_names = ['beverage_length', 'beverage_width', 'price_length', 'price_width', 'kind']

    feature_names = column_names[:-1]
    label_name = column_names[-1]

    print("Characteristic: {}".format(feature_names))
    print("Labels: {}".format(label_name))

    # creating Dataset

    batch_size = 32

    train_dataset = tf.data.experimental.make_csv_dataset(
        train_dataset_fp,
        batch_size,
        column_names=column_names,
        label_name=label_name,
        num_epochs=1)

    features, labels = next(iter(train_dataset))

    print(features)

    # Checking data from batch
    plt.scatter(features['beverage_length'],
                features['price_length'],
                c=labels,
                cmap='viridis')

    plt.xlabel("beverage_length")
    plt.ylabel("price_length")
    plt.show()

    train_dataset = train_dataset.map(pack_features_vector)

    features, labels = next(iter(train_dataset))

    print(features[:5])

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)),
        tf.keras.layers.Dense(10, activation=tf.nn.relu),
        tf.keras.layers.Dense(3)
    ])

    predictions = model(features)
    # show 5 samples
    predictions[:5]

    tf.nn.softmax(predictions[:5])

    l = loss(model, features, labels)
    print("Loss test: {}".format(l))

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

    loss_value, grads = grad(model, features, labels)

    print("Step: {}, initial loss: {}".format(optimizer.iterations.numpy(),
                                              loss_value.numpy()))

    optimizer.apply_gradients(zip(grads, model.trainable_variables))

    print("Step: {},      loss: {}".format(optimizer.iterations.numpy(),
                                           loss(model, features, labels).numpy()))

    # Running this cell again uses variables from the same model.
    train_loss_results = []
    train_accuracy_results = []

    num_epochs = 201

    for epoch in range(num_epochs):
        epoch_loss_avg = tf.keras.metrics.Mean()
        epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
        for x, y in train_dataset:
            loss_value, grads = grad(model, x, y)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))
            epoch_loss_avg(loss_value)
            epoch_accuracy(y, model(x))

    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 50 == 0:
        print("Epoch {:03d}: loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                    epoch_loss_avg.result(),
                                                                    epoch_accuracy.result()))

    # ref : https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough


SoftMax()