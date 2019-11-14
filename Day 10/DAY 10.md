# DAY 10

***


## 1.Sigmoid 

***

 ![img](https://t1.daumcdn.net/cfile/tistory/99B9A3335981FCAC0F) 





 ![(X축:-5, Y축:0) → (X축:0, Y축:0.5) → (X축:5, Y축:1)](https://icim.nims.re.kr/file/1d96aff862744eef892c8c8027159935.jpg) 





##### ◎Characteristic 

1> Result is limitied to [0,1]

2> Used similarly to neurons in the brain



##### ◎Problem

1> Gradient dies (Gradient vanishing problem) 

2> The center of the resulting function is 0.5, not 0

3> Computation is complicated (exponential calculation) 

 

※ vanishing problem : The more hierarchies, the more difficult it is to learn. 



## 2.reLU
***


- The ReLU function stands for Rectified Linear Unit. 



 ![img](https://t1.daumcdn.net/cfile/tistory/990A6A335981FFA437) 



◎Characteristic 

1> Active Functions Most Popular in Recent Neural Networks

2> It is considered nonlinear because it bends at zero.

3>**Unlike the sigmoid, the derivative is not less than 1, so the slope does not disappear even if multiplied by any number**



 ![img](https://t1.daumcdn.net/cfile/tistory/25414C47579F7BC229) 







## 3.Weight

***



##### There are difference in cost function depending on what value we initialize as first weight

------



- ### How to initialize first weight



1. ##### Never give 0

   If we initialize to 0, every input value becomes to 0

2. ##### Restricted Boatman machine

   **Goal** : to recreate input

   **Forward** : Given input * weight, make next value = encode
   **Backward** : Next value * (weight^-1), recreate Given input = decode

   **Recreate** : Forward & backward

   **How to initialize** : Compare first given input & recreated input, to make these two values as same as possible.

    ![img](https://postfiles.pstatic.net/MjAxOTExMTJfMTU0/MDAxNTczNTY1Mjg3NzY3.Llax6ZMSXxLN9Dd8Qy4enG-WDXLiZL1xJGPbMF3_R9cg.MN1nKZhd41NLOzb91EcKE3tRXduGVzHeZd7vJafAdYcg.PNG.smreo123/image.png?type=w773) 

   **Neural network** : Initialize each weight per two layers of neural network

    ![img](https://postfiles.pstatic.net/MjAxOTExMTJfMjM4/MDAxNTczNTY1NDU1OTM2.R7YkM7gix1BSvGgapV0h5Xj9uPJ4PTM0bNDB-wYDkN4g.HguXj8sEEr2RLVtKhkHw9OoheXpGk4xaAuUtRRq5hXUg.PNG.smreo123/image.png?type=w773) 

3. ##### Xavier initialization / He's initialization

   RBM is to complicated, and these initialization algorithm achieves higher performance

   **theory** : Initialize weight by the number of input value & output value per node

   `W = np.random.randn(fan_in,fa_out) / np.sqrt(fan_in)`

   => **Xavier initialization**

   `W = np.random.randn(fan_in,fa_out) / np.sqrt(fan_in/2)`

   => **He's initialization**

   ------

   

- ### Performance

  

 ![img](https://postfiles.pstatic.net/MjAxOTExMTJfMTcx/MDAxNTczNTY1NjUzNjA0.vdtj4B7oxj_5bzyUZgZK7uSLzZ7l6jnZtrFQc19YyQYg.ydVPZgIoWPI2vE-vEErAmjExwFi7kyncOgGxQGD0GYwg.PNG.smreo123/image.png?type=w773) 

------



- ### Highly possibility research area

**Previous research achieved high performance**
**But there are more possibility to develop higher performance algorithm than the previous**


## 4.Dropout
***

Over-optimizing the training data is called <b>overfitting</b>.

The deeper the Neural Network, the more likely it is to be overfitting. This is because there are more variables, and accordingly more classification criteria.

One of solution is <b>dropout</b>.

<b>Dropout</b> is a regularization techique for reducing overfitting in neural networks by preventing complex co-adaptations on training data. It is a very efficient way of performing model averaging with neural networks. The term "dropout" refers to dropping out units (both hidden and visible) in a neural network.

![](https://miro.medium.com/proxy/1*iWQzxhVlvadk6VAJjsgXgg.png)

Inherently fully connected, the interrelationships between nodes are quite complex. But if you don't go through all the nodes through dropout, you get a sparse network as shown on the right.

In TensorFlow, 
* We create a disconnect node in the middle of the node and put it in the middle.
* Set the dropout rate at the time of learning(almost 0.5).
* When it is time to evaluate, set the dropout rate to 1 so that all nodes do not rest.

## 5.Ensemble
***

![](https://i.pinimg.com/originals/4b/83/e4/4b83e452f1dfbfbade8b8c5a58256f02.jpg)

If you have a lot of data and a lot of computers, you can use the <b>ensemble method</b>. By dividing the data into several training sets and learning at the same time, after the training for all the training set is a method of integrating the results.

<b>Ensemble</b> seems to be a legitimate way to get advice from several experts at the same time. Using this method improves performance by at least 2% to 4-5%. It is similar to dropout in that it produces balanced results over several attempts.

### Reference
***
[ko]https://www.youtube.com/watch?v=wTxMsp22llc&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=33&t=0s

