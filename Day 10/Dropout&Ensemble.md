# Day 10

## 4.Dropout
***

Over-optimizing the training data is called <b>overfitting</b>.

The deeper the Neural Network, the more likely it is to be overfitting. This is because there are more variables, and accordingly more classification criteria.

One of solution is <b>dropout</b>.

<b>Dropout</b> is a regularization techique for reducing overfitting in neural networks by preventing complex co-adaptations on training data. It is a very efficient way of performing model averaging with neural networks. The term "dropout" refers to dropping out units (both hidden and visible) in a neural network.

![image.png](attachment:image.png)

Inherently fully connected, the interrelationships between nodes are quite complex. But if you don't go through all the nodes through dropout, you get a sparse network as shown on the right.

In TensorFlow, 
* We create a disconnect node in the middle of the node and put it in the middle.
* Set the dropout rate at the time of learning(almost 0.5).
* When it is time to evaluate, set the dropout rate to 1 so that all nodes do not rest.

## 5.Ensemble
***

![image.png](attachment:image.png)

If you have a lot of data and a lot of computers, you can use the <b>ensemble method</b>. By dividing the data into several training sets and learning at the same time, after the training for all the training set is a method of integrating the results.

<b>Ensemble</b> seems to be a legitimate way to get advice from several experts at the same time. Using this method improves performance by at least 2% to 4-5%. It is similar to dropout in that it produces balanced results over several attempts.

### Reference
***
[ko]https://www.youtube.com/watch?v=wTxMsp22llc&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=33&t=0s
