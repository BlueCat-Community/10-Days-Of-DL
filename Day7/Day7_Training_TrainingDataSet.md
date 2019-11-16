# Day 07
### Learning and test data sets

----------

#### how to evaluate the model is good
To evaluate a model, data is put into a model that is built on a training set 
to be determined from its prediction. 

But if we learn from all the data we have, there is no set of data to evaluate the model. 

Therefore, predictions used by the datasets used for learning will be evaluated 
to be nearly 100% accurate. 

This is exactly not good way.


#### Test set
Part of the dataset is divided into test sets. and test set is not used for learning

We evaluate the model that was learned by training set with test set. 

We set as a result of putting test set into model is  y̅ , the actual value of test set is y and 
compare these two values so that we can get accuracy

#### Validation set

When we train with hyperparameter such as α or λ  , we don't know which hyperparameter value gives us better result

The part of training set is set validation set, we tune the hyperparameter with validation set

 ![img](https://www.intechopen.com/media/chapter/39037/media/image3.jpeg) 



#### Online learning

When there're lots of dataset to train, there can be Out-Of-Memory error or etc.

We divide the dataset into several parts, training them sequentially is online learning

As a part of dataset is finished to train, the result value is saved in model.

The each result value makes final model.

 ![img](https://postfiles.pstatic.net/MjAxOTEwMzBfNSAg/MDAxNTcyNDQ0Mjk2NjQy.-ZnXkqnqvH_DTm4n0xb_kICbOhr1bJODwp8ZdwnUD0og.NvK6k87x0P1mJmHk4c-rygmrGQt6wujswC3hkQA7kD0g.PNG.smreo123/image.png?type=w773) 
