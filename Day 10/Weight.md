# Weight

------



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