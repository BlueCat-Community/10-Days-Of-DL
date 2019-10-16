# Day 3



### 1. Linear Regression's cost minimize algorithm

---

<b>1) Condition Precedent</b>

> <b>Convex Function</b>
> 							<img width="298" alt="lec03_1" src="https://user-images.githubusercontent.com/32675267/66925591-998d9000-f067-11e9-850c-afa4b9e2bbc0.PNG">
> We have to check if cost function is in convex figure.
> At cost function like left side, we cannot check minimum point of function by gradient descent. 
> So the function have to be in figure like right side.

> <b>Convex Graph</b>

> To minimize the cost function, we want to know  which point(W,b) can minimize the cost function.
> We will simplify the Hypothesis Hx for concentrating on W value of it.
> 							<img width="255" alt="lec03_2" src="https://user-images.githubusercontent.com/32675267/66925643-aca06000-f067-11e9-9a41-254429f94427.PNG">



---



To optimize <b>Linear Regression</b>, <b>Cost</b> must have a minimum value. That's why we need to find a case where cost is the minimum. In this case, we use a cost minimization algorithm. A typical example of which is <b>Gradient Descent Algorithm</b>.



We used a hypothesis above. But to simplify the equation, we will change the hypothesis formula a bit.

<img src="https://user-images.githubusercontent.com/32675267/66719086-437dda00-ee26-11e9-9726-3fd9633063f3.png" alt="ch_hy" style="zoom:48%;" />

<img src="https://user-images.githubusercontent.com/32675267/66719092-509ac900-ee26-11e9-8a64-84f9ec433b6c.png" alt="ch_hy2" style="zoom:48%;" />

We can see this <b>Cost Function</b> with graph.

<img src="https://user-images.githubusercontent.com/32675267/66719099-5f817b80-ee26-11e9-9f90-367dfff673c0.PNG" alt="min" style="zoom:48%;" />





<b>2) Gradient Descent Algorithm</b>

<b>Gradient Descent Algorithm</b> finds the minimum value by descending along the slope of the graph.

> 1. Pick any point on the graph.
> 2. Find the slope of the selected point.
> 3. Change the values of W and b to find the point where the slope is reduced the most.
> 4. Repeat the above process to find the minimum.

> * At the minimum, the slope is zero.
>
> * The formula below shows Gradient Descent Algorithm.
>
> <img src="https://user-images.githubusercontent.com/32675267/66719107-6d370100-ee26-11e9-85aa-5cd867f65f40.png" alt="gd" style="zoom:75%;" />
>
> * a : Learning rate 
>
>     - How much will it go down
>    
>     - Big learning rate: no converge
>    
>     - Small learning rate : Find minimum but too slow
>    
>
> ![learning rate](https://user-images.githubusercontent.com/44569994/66711199-58c11d00-edc2-11e9-9fd7-6ff5fbf4b11c.png)



<img src="https://user-images.githubusercontent.com/32675267/66719115-7a53f000-ee26-11e9-9cd8-c3138113229e.png" alt="fin" style="zoom:48%;" />