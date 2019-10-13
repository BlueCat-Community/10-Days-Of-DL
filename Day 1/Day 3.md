# Day 3



### 1. Linear Regression's cost minimize algorithm

---

To optimize <b>Linear Regression</b>, <b>Cost</b> must have a minimum value. That's why we need to find a case where cost is the minimum. In this case, we use a cost minimization algorithm. A typical example of which is <b>Gradient Descent Algorithm</b>.



We used a hypothesis above. But to simplify the equation, we will change the hypothesis formula a bit.

<img src="img\ch_hy.png" alt="chhy" style="zoom:48%;" />

<img src="img\ch_hy2.png" alt="ch2" style="zoom:50%;" />



We can see this <b>Cost Function</b> with graph.

<img src="img\min.PNG" alt="min" style="zoom:48%;" />





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
>   <img src="img\gd.png" alt="GD" style="zoom:75%;" />



<img src="img\fin.png" alt="fin" style="zoom:48%;" />

