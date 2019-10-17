# Day 04
### Multi-variable linear regression

----------

> The previously learned Hypothesis, Cost function, and Gradient Descent algorithm are utilized.

#### Hypothesis

In multi-variable linear regression, we can show the hypothesis like this:  

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571304553462_image.png)

![hypothesis using matrix](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571304633691_image.png)

And we can simplify the multi-variable linear regression using matrix multiplication.
  

#### Cost function

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571305831093_image.png)

When implementing the equation using TensorFlow, we usually place X in front of W  

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571304279299_image.png)

It is the order of X and W that should be noted. When expressing by multiplying the matrix, it should be done in the order of X and W.
  

We have to design this W for the most part.

![](https://paper-attachments.dropbox.com/s_016A76D72A71A96120AC235F5771E6E5FBB3333CEB56627F1CE918202DE8727D_1571305285849_image.png)

Then you can look at X and H(X).
The size of X and H(X) is given, and the nature of this dot product shows that W is [3, 1].

![](https://paper-attachments.dropbox.com/s_7E65FAD9F079BD5BE143B324B94A80F212B2386BA05CFF3B9661484B89459E8B_1571305198942_image.png)


#### Lab

Matrix X's rows are: **instances**  
We can use n instances in the matrix.
so, we use n, -1, None to illustrate that there can be any number of instances in X  
> ex) [n, 3]  
  
Matrix X's columns are: **variables**
When conducting matrix multiplication,  [a, b] [c, d],  
the result matrix is [a, d]
and b must be the same value as c in order to conduct multiplication
  
**Slicing**  
list[x:y] -> get the elements of the list, from index x to y-1.  
empty x or y means -> all of the elements
negative elements means -> to the inverse index of elements
![](https://user-images.githubusercontent.com/43871679/66986482-fcc80280-f0f9-11e9-9e2c-0e77b3f1e917.png)
  
**Reference**
[https://www.youtube.com/playlist?list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm](https://www.youtube.com/playlist?list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm)