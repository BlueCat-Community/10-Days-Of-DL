# Day 1



### 1. Machine Learning

***

<i><b>Machine Learning</b></i>  is a field of development that was born due to limitations in expect programming, a program in which developers set rules. It is a development area where programs can automatically learn rules and learn for themselves.



<img src="img\machine.png" alt="Machine Learning" style="zoom:40%;" />



---



##### 1) Supervised Learning

This is a method of progressing learning <u>_with labeled data_</u>.

<i>Labeled data</i> means that input data and output data are predefined. This data is called <b>training data</b>. After training with this <b>training data</b>, we can measure how accurate the algorithm is through the <b>testing data</b>.



<img src="img\supervised.png" alt="Supervised" style="zoom:40%;" />

​	

> <b>Regression</b>
>
> It is a way of predicting <u>continuous valued</u>. 
>
> <i>Ex) To predict student's test scores.</i>



> <b>Classification</b>
>
> It it a way of predicting <u>categorical valued</u>.
>
> > <b>Binary Classification</b>
> >
> > Category is only two, for example (yes / no) or (1 / 0).
> >
> > <i>Ex) To predict student's pass of fail.</i>
>
> > <b>Multi-Class Classification</b>
> >
> > It has many category, for example (Small / Medium / Large).
> >
> > <i>Ex) To predict student's grade, for example (A / B / C / D/ F).</i>



##### 2) Unsupervised Learning

This is a method of progressing learning <u>_without a label for data_</u>.

It is often used to discover hidden features or structures of data.



> <b>Clustering</b>
>
> This is a method of grouping data with similar characteristics.





### 2. Linear Regression

___

This algorithm belongs to <b>Supervised Learning</b>. It is an algorithm that starts learning with the assumption that a linear graph is appropriate for the data we are going to learn.

---



<b>1) Hypothesis</b>

Because <b>regression</b> is a way of learning from data, we need to define a <i>hypothesis</i> about the data before we start learning. We need to formulate a linear equation for <b>Linear Regression</b>.



<img src="img\hypothesis.png" alt="Hypothesis" style="zoom:60%;" />

> When input <b>x value</b> to this hypothesis then we can gain <b>predicted  y value</b>.



<b>2) Cost Function</b>

We must determine whether our <b>hypothesis</b> is appropriate or not. When we determine this, we use <b>Cost Function</b>. This formula means <b>Cost Function</b>.

~~~
(H(x) - y)^2
~~~

This formula means, find and square the difference between the predicted and actual values. We use squares to rule out negative numbers and to give greater penalties.

<b>Cost</b> is the average of the above values.  <b>Cost</b> can be expressed as a formula.

<img src="img\cost1.png" alt="Cost1" style="zoom:75%;" />

<i>H(x)</i> equal with <i>Wx + b</i>. So, it is same with below formula.

<img src="img\cost2.png" alt="cost2" style="zoom:75%;" />

##### TO optimize Linear Regression, the cost value should be minimum.





### 3. Linear Regression's cost minimize algorithm

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

