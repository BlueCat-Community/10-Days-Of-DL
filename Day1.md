### 1. Machine learning basic


<B>학습을 하는 방법</B>

1. suprvised : 라벵이 정해져 있는 데이터를 학습 예시) 라벨링 된 이미지 학습 후, 라벨링
    
    --결과에 따라서--
    
    1) regression
    
    2) binary classification
    
    3) multi-label classfication
     

2. unsupervised:: 라벨이 정해져 있지 않는 데이터 보고 스스로 학습 예시) 구글 뉴스 그룹핑


-----


<B> Tensorflow lab</B>

tensorflow node 

1. constant : 상수를 저장 하는 데이터 형태
    
    ```python
    import tensorflow as tf
    a=tf.constant([5]) 
    ```
    
2. Variable : 변수를 저장 하는 데이터 형태
             버전 1- 변수 초기화 필수 : global_varaibales_initializer()
             버전 2- 변수 초기화X
            
            
   ```python
    import tensorflow as tf
    tf.Variable(tf.random.normal([4,2]))
    sess=tf.Session() 
    sess.run(tf.global_varaibales_initializer())
    ```


3. palceholder : 데이터를 담는 그릇
                 데이터 넣기 -feed 
    
    ```python
    import tensorflow as tf
    x=tf.placeholder(dtype=tf.float32)
    sess=tf.Session()
    result=sess.run(x,feed_dict={x:[1,2,3]}
    ```


**tensorflow 버전 2 차이점**

1) Session (): 사용 X,
2) tf. function 데코레이터 사용 가능
3) Variable 변수 초기화 필요 X
4) placeholder , fedd_dict : 일반 함수 호출시 매게 변수로 


## 2. Linear Regression

----

하나의 가설을 세워서 값을 예측

H(X)=wx+b

![image.png](https://user-images.githubusercontent.com/44569994/66707114-bb8cc700-ed76-11e9-86ad-299e0939b697.png)

이 중에서 가설을 선택 하는 기준 필요 

--> <B><i>cost function</i></B>

---


**Cost function**
1. 실제 값하고 예측 한 값의 차의 합 평균 (Mean Squared)

![costfunction.png](https://user-images.githubusercontent.com/44569994/66707088-6650b580-ed76-11e9-8215-ff70dff14b7d.png)

![example](https://user-images.githubusercontent.com/44569994/66707123-d101f100-ed76-11e9-88ed-e44d7251a989.png)

--> 왼쪽 가설 선택


-----


### 3. Minimize cost function

linear regression -> cost function이 최소화 되는 가설을 찾는 것.
<B> cost function 최소화 방법 </B>

1. Gradient descent algorithm
: 랜덤 값의 w를 지정하고, 그 지점 부터 경사를 따라 내려오는 알고리즘
![GDA](https://user-images.githubusercontent.com/44569994/66711142-37136600-edc1-11e9-91c5-2e3bfd7b1f57.png)


* a : learning rate 

    -얼마 만큼 내려 갈것 인지
    
    -큰 learning rate: 수렴 되지 않을 수 있다.
    
    -작은 learning rate : mimimum을 찾지만, 시간이 너무 오래 걸린다.
    
    ![learning rate](https://user-images.githubusercontent.com/44569994/66711199-58c11d00-edc2-11e9-9fd7-6ff5fbf4b11c.png)

* gradient descent 를 사용하기 위해서는 cost function이 convex function (모든 점에서 다음과 같은 식이 성립
![convex.png](https://user-images.githubusercontent.com/44569994/66711160-b143ea80-edc1-11e9-9776-fd6fa24e32e9.png)

