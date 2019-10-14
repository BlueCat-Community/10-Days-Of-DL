# Day 3



### 1. Linear Regression's cost minimize algorithm

---

To optimize <b>Linear Regression</b>, <b>Cost</b> must have a minimum value. That's why we need to find a case where cost is the minimum. In this case, we use a cost minimization algorithm. A typical example of which is <b>Gradient Descent Algorithm</b>.



We used a hypothesis above. But to simplify the equation, we will change the hypothesis formula a bit.

<img src="https://user-images.githubusercontent.com/32675267/66719086-437dda00-ee26-11e9-9726-3fd9633063f3.png" alt="ch_hy" style="zoom:48%;" />

<img src="https://user-images.githubusercontent.com/32675267/66719092-509ac900-ee26-11e9-8a64-84f9ec433b6c.png" alt="ch_hy2" style="zoom:48%;" />

We can see this <b>Cost Function</b> with graph.

<img src="https://user-images.githubusercontent.com/32675267/66719099-5f817b80-ee26-11e9-9f90-367dfff673c0.PNG" alt="min" style="zoom:48%;" />





<b>1) Gradient Descent Algorithm</b>

<b>Gradient Descent Algorithm</b> finds the minimum value by descending along the slope of the graph.

> 1. Pick any point on the graph.
> 2. Find the slope of the selected point.
> 3. Change the values of W and b to find the point where the slope is reduced the most.
> 4. Repeat the above process to find the minimum.

> * At the minimum, the slope is zero.
>
> * The formula below shows Gradient Descent Algorithm.
>
>   <img src="https://user-images.githubusercontent.com/32675267/66719107-6d370100-ee26-11e9-85aa-5cd867f65f40.png" alt="gd" style="zoom:75%;" />



<img src="https://user-images.githubusercontent.com/32675267/66719115-7a53f000-ee26-11e9-9cd8-c3138113229e.png" alt="fin" style="zoom:48%;" />