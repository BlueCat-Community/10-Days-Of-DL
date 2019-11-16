# 1. SoftMax Regression 

1. ###### What is it ? 

   : SoftMax Regression is a learning method for classifying logistic classification into serveral groups.

   

   

2. ###### Characteristic 

   1> It has a value between 0 and 1.

   2> The total sum is one. 

   

   ![Fig. 2. A graphical illustration of the training principle for our soft regression based early action prediction framework. In this framework, we develop a novel online RGB-D action feature extractor and a soft regression model. The early action predictor and soft labels are learned jointly. In the figure, operator ⊗ is a Kronecker product and for the loss computation. Each curve in the second block (from the left hand side) corresponds to one dimension of the computed integral features. For clarity and simplicity, we only present a small set of the extracted integral features.](https://d3i71xaburhd42.cloudfront.net/c9b958c2494b7ba08b5b460f19a06814dba8aee0/3-Figure2-1.png) 

   
   
   ( https://www.semanticscholar.org/paper/Early-Action-Prediction-by-Soft-Regression-Hu-Zheng/c9b958c2494b7ba08b5b460f19a06814dba8aee0/figure/2 )
   
   

# 2. Cost Fucntion 

###### 1. What is it ?

: It is a function that Shows the difference between the predicted value and the actual value 





###### 2. Characteristic  

   1> For the correct answer, the value of Cost is zero. 

   2>If not correct, the cost goes to infinity. 



 		**Cost function (J) = 1/m (Sum of Loss error for ‘m’ examples)** 

 ![cost function with one optima](https://engmrk.com/wp-content/uploads/2018/05/cost-function-with-one-optima.jpg) 

( https://engmrk.com/error-and-cost-function-for-nn/ )



# 3. Reference

-  https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough#the_iris_classification_problem 

