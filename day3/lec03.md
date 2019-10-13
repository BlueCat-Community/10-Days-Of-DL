# [lec03]linear regression cost minimization
we will learn about how to minimize the cost function of Linear Regression model <i>Cost(W,b)</i>
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03costfunc.png" style="zoom:40%;"/> 
***
### 1) Condition Precedent
> <b>Convex Function</b>
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03convexfunc.PNG" style="zoom:40%;"/> 
We have to check if cost function is in convex figure.
At cost function like left side, we cannot check minimum point of function by gradient descent. 
So the function have to be in figure like right side.

> <b>Convex Graph</b>
> To minimize the cost function, we want to know  which point(W,b) can minimize the cost function.
> We will simplify the Hypothesis Hx for concentrating on W value of it.
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03funcsimplify.PNG" style="zoom:40%;"/> 

When we simplify Hypothesis into H(x), we can transfer the 3-dimensional convex function graph into 2-dimensional convex graph. So we just have to find the minimum W point at the graph to minimize the cost. We will use gradient descent algorithm at here.
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03convexgraph.PNG" style="zoom:40%;"/> 

---
### 2) Gradient Descent
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec3gradientDescent.PNG" style="zoom:40%;"/>
Gradient Descent is way to find the minimum point of the convex graph by checking where slope(W) of the cost function changed gradientially. 
​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03costGradientMinimize.png" style="zoom:40%;"/> 
We can use two methods to <b>calculate the minimum slope(W) of the cost function.</b>
> 1)Take Differentiation 
> 2)Use GradientDescentOptimizer function

---
### 3) Differentiation(미분)

​							<img src="https://github.com/teddy309/10-Days-Of-DL/blob/master/day3/images/lec03formalW.png" style="zoom:40%;"/> 

This is 3 step process to get differentiation of slope(W). Result of differentiation is same as W above.
