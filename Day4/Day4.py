import tensorflow as tf
import numpy as np
print(tf.__version__)

#dataset
X_train = [[73.,80.,75.],[93.,88.,93.],[89.,91.,90.],[96.,98.,100.],[73.,66.,70.]]
y_train = [[152],[185],[180],[196],[142]]

#make class
class multi_linear(object):    
    #inicialization
    def __init__(self, learning_rate=1e-5):
        self.W = tf.Variable(tf.random.normal([3,1]),name='weight')
        self.b = tf.Variable(tf.random.normal([1]),name='bias')
        # make optimizer that use Gradient descent
        self.optimizer = tf.keras.optimizers.SGD(lr=learning_rate)
    
    #compute cost and find best parameter   
    def fit(self, X, y, epochs=20):
        #epoch : count of learning in machine learning
        cost = []
        for i in range(epochs):
            #make calculation method of cost and save result
            with tf.GradientTape() as tape:
                predict_y = tf.matmul(X,self.W)+self.b
                sqr_errors = tf.square(y - predict_y)
                mean_cost = tf.reduce_mean(sqr_errors)
            #compute gradient
            grads = tape.gradient(mean_cost, [self.W, self.b])
            # find least cost using optimizer
            self.optimizer.apply_gradients(zip(grads, [self.W, self.b]))
            cost.append(mean_cost)
        return cost
    
    #return predicted value
    def predict(self, X):
        return tf.matmul(X,self.W)+self.

#make model
model = multi_linear()
costs = model.fit(X_train, y_train)

#make graph
import matplotlib.pyplot as plt
plt.plot(range(1,len(costs) + 1), costs)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.show()
value_predict=model.predict(X_train)

#compare real value and predicted value
for i in range(5):
    print("target value : ",y_train[i], " predicted value : ",value_predict[i])
