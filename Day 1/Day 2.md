# Day 2



### 1. Linear Regression

___

This algorithm belongs to <b>Supervised Learning</b>. It is an algorithm that starts learning with the assumption that a linear graph is appropriate for the data we are going to learn.

---



<b>1) Hypothesis</b>

Because <b>regression</b> is a way of learning from data, we need to define a <i>hypothesis</i> about the data before we start learning. We need to formulate a linear equation for <b>Linear Regression</b>.



<img src="https://user-images.githubusercontent.com/32675267/66719065-07e31000-ee26-11e9-91e5-4b83c97b7b0b.png" alt="hypothesis" style="zoom:60%;" />

> When input <b>x value</b> to this hypothesis then we can gain <b>predicted  y value</b>.



<b>2) Cost Function</b>

We must determine whether our <b>hypothesis</b> is appropriate or not. When we determine this, we use <b>Cost Function</b>. This formula means <b>Cost Function</b>.

~~~
(H(x) - y)^2
~~~

This formula means, find and square the difference between the predicted and actual values. We use squares to rule out negative numbers and to give greater penalties.

<b>Cost</b> is the average of the above values.  <b>Cost</b> can be expressed as a formula.

<img src="https://user-images.githubusercontent.com/32675267/66719072-20532a80-ee26-11e9-8f6b-5ded8d374c47.png" alt="cost1" style="zoom:75%;" />

<i>H(x)</i> equal with <i>Wx + b</i>. So, it is same with below formula.

<img src="https://user-images.githubusercontent.com/32675267/66719078-2cd78300-ee26-11e9-8fa9-2666420837e1.png" alt="cost2" style="zoom:75%;" />

##### TO optimize Linear Regression, the cost value should be minimum.