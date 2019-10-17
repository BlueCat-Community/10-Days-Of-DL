# Day 04
### Logistic classification

----------

#### Motivation
In day 3 and day 4, we studied regression about predict numeric value. But what if we want to predict the response value with a binary value(0 or 1, yes or no ..)? show the graph.

![](https://paper-attachments.dropbox.com/s_1E08A6CC3FA9A77A760B58710BF71082557C2704B42AD00154B3AE74F8064317_1571305424283_1.png)


This graph is the result of linear regression. 
Target attribute have binary value(Yes or No). As you can see the result is bad.
0, 1 encoding could be conducted at the same time to conduct classification using categorical values.  
  

#### Case of application
- Spam Detection : Spam or Ham
- Facebook feed : show or hide
- Credit Card Fraudulent Transaction detection : legitimate or fraud

#### Cons of classification

- Not as sensitive as regression, since it uses labels instead of continuous target value
- Cannot handle hypothesis with values larger than 1 or less than 0.

#### Sigmoid function
Sigmoid function is used in logistic classification. it curved in two dimension.

![](https://paper-attachments.dropbox.com/s_1E08A6CC3FA9A77A760B58710BF71082557C2704B42AD00154B3AE74F8064317_1571305547264_2.png)

![sigmoid](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571305369035_image.png)


The y-axis value of the sigmoid function has a value between 0 and 1.
** This is the main reason used in logistic classification. **

#### Hypothesis of logistic classification
So let's go find the hypothesis of logistic classification.
Sigmoid function's x-axis is z.
Insert WX to z's position. -> we get H(x)=(z)
We get logistic classification's hypothesis.

#### New cost function for logistic

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571306169188_image.png)


If the actual value is similar to the predicted value, cost should be low!
In new cost function for logistic,

1. y=1: cost is close to ‘0’.
2. y=0: cost is increasing to infinite.

##### Remove If condition

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571305519130_image.png)


If y=1, c= -log(H(x)) equal to previous equation.
If y=0, c=-1*log*1-H(x)), equal to previous equation.


#### Gradient decent algorithm (Minimum cost)


![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571305889445_image.png)

