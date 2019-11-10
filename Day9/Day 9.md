# Day 9
**Today we will talk about how to solve the *XOR problem*.**
  

### 1. Solving XOR problems with deep learning
***
Logistic regression can choose only one of two results(0 or 1). Therefore, using only one logistic regression cannot solve the XOR problem. However, using three logistic regression can solve the problem.

![NN](https://user-images.githubusercontent.com/37873745/68453389-be28f200-0238-11ea-82ce-eec8d2fb65c2.png)

Let's solve the XOR problem by using NN with 3 logistic regression.

![XOR](https://user-images.githubusercontent.com/37873745/68453390-be28f200-0238-11ea-801f-0420be87f482.png)

As mentioned earlier, we used three logistic regressions. In each classifier, w, b, and S exist, and S means 'Sigmoid function'. That means the result is only zero and one. **An important part of this figure is that the results (y1 and y2) of the first and second logistic regression are used for the third logistic regression.** Calculate the regression using w and b, put it in the sigmoid function and get the results. As a result, you will see that the XOR results come from the last third logistic regresion.

![](https://user-images.githubusercontent.com/43871679/68417050-03b5d280-01d9-11ea-809f-847764749934.PNG)
The preceding figure and process can be expressed as shown in the above figure, provided that they are presented in a simple illustration.
The first x1 and x2 are passed to two logistic regression, and their calculation results are passed to the input of the last logistic regression.

![NN_multinomial](https://user-images.githubusercontent.com/37873745/68453901-3d6af580-023a-11ea-8f16-790873381ecf.png)

Let's now translate this into a multinomial classification.
When converting a previous logistic revision to a multinomial classification, it was processed using **a matrix**. Again, the initial values, W, and b, can be expressed as shown in the above figure. In one step, multiple logistic regression can be expressed and performed together, which is called **a layer**.
So far, we have discussed how to solve the XOR problem through NN. **So how can we learn W and b from training data?**
  
  
### 2. Backpropagation

***

The Neural Network is configured to have multiple layers to solve complex problems. **The first layer is called the input layer, the last layer is called the output layer, and every layers in the middle are called the hidden layer.** The hidden layer is invisible, so there are drawbacks that are difficult to identify inside. In severe cases, you may not understand how it works.
However, using **derivative** can solve this problem. If you can see how the front layer affected the back layer, the reverse can also be seen.

![Backpropagation](https://user-images.githubusercontent.com/37873745/68453384-bd905b80-0238-11ea-8764-947a924f7367.png)

It is called forward propagation when switch W and b from the front and backward propagation when change from the back to the front.
Of the multiple layers in the Neural Network, the most significant influence on the results becomes the later layers. In conclusion, making only a fraction of the layers at the back can make even better predictions.

***

There are some details about the derivative from here. If you don't know about the derivative, please go to the address below and be familiar with the derivative.

https://www.youtube.com/watch?v=GzphoJOVEcE&

***

![XORBackpropagation_chain_rule](https://user-images.githubusercontent.com/37873745/68453385-bd905b80-0238-11ea-8473-a9ca0f995732.png)

Let's find out how much f changes when there are w,x,b,g values to know about backpropagation.
- f = wx + b
- If g = wx, it can be expressed as f = g + b.
  
Let's first look at g. If you differentiate by x for g, you can see the change in g as x changes. If you differentiate by w for g, the amount of g changes as w changes.
Let's see f this time. Let's differentiate f by w. Then the change of w will result in the change of g, and through it you will see the change of f. Likewise, the differential of f to x changes g, and through it you can see the change of f.
**The first w and x correspond to the input layer, the last f to the output layer, and the middle g to the hidden layer.** When I modified the value in the input layer, I could calculate how the value in the output layer changes. Although simple, this is how the backpropagation algorithm works.


![BackpropagationXOR](https://user-images.githubusercontent.com/37873745/68453386-be28f200-0238-11ea-8601-0ab9a37933ca.png)

**Chain rule**
![chain_rule](https://user-images.githubusercontent.com/37873745/68453687-b0c03780-0239-11ea-9793-ced8be7494c3.png)

![Backpropagation](https://user-images.githubusercontent.com/37873745/68453387-be28f200-0238-11ea-9315-82e62b5b14af.png)
A simple representation of the above process can be expressed in the above figure.
  
  
### 3. Reference
***
[ko]https://www.youtube.com/watch?v=GYecDQQwTdI&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=25
[ko]https://www.youtube.com/watch?v=573EZkzfnZ0&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=27
https://medium.com/@jayeshbahire/the-xor-problem-in-neural-networks-50006411840b
https://medium.com/analytics-vidhya/understanding-basics-of-deep-learning-by-solving-xor-problem-cb3ff6a18a06
https://www.youtube.com/watch?v=gl3lfL-g5mA&