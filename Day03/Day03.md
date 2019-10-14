### 3. Minimize cost function

linear regression -> finding the hypothesis that cost function is minimized

<B> How to minimize "cost function" </B>

1. Gradient descent algorithm
:algorithm that assign random values and follw slope from that point to finding minimum

![GDA](https://user-images.githubusercontent.com/44569994/66711142-37136600-edc1-11e9-91c5-2e3bfd7b1f57.png)


* a : learning rate 

    - how much will it go down
    
    - big learning rate: no converge
    
    - small learning rate : find minimum but too slow
    

![learning rate](https://user-images.githubusercontent.com/44569994/66711199-58c11d00-edc2-11e9-9fd7-6ff5fbf4b11c.png)


* For using gradient descent, cost function is must convex function (for every point , the following equation is established)


![convex.png](https://user-images.githubusercontent.com/44569994/66711160-b143ea80-edc1-11e9-9776-fd6fa24e32e9.png)

