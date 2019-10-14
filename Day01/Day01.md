### 1. Machine learning basic
<B>Way of learning</B>

1. suprvised : training with labeled data  ex) labeling
    
    --Accoding to result--
    
    1) regression
    
    2) binary classification
    
    3) multi-label classfication
     

2. unsupervised: training with no labeled data ex) grouping
                 
                 



-----


<B> Tensorflow lab</B>

tensorflow node 

1. constant : data types that store constant
    
    
    ```python
    import tensorflow as tf
    a=tf.constant([5]) 

    ```
    
2. Variable : data types that store variable
             
             * in version 1.x- must variable initialization : using tensorflow.global_varaibales_initializer()
             * in version 2- no variable initialization
            
            
   ```python
    import tensorflow as tf
    tf.Variable(tf.random.normal([4,2]))
    sess=tf.Session() 
    sess.run(tf.global_varaibales_initializer())
    ```


3. palceholder : data types that data container
                 add data -feed 
    
    ```python
    import tensorflow as tf
    x=tf.placeholder(dtype=tf.float32)
    sess=tf.Session()
    result=sess.run(x,feed_dict={x:[1,2,3]}
    ```


**Dffirence tensorflow version 2**

1) Session () X

2) tf. function decorator

3) no variable initialization

4) placeholder , fedd_dict : when calling a gnenral function, use the parameter

