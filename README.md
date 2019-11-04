# 10-Days-Of-DL 
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

- **tensorflow 2.0 을 이용한 10일 완성 deep learning**
- **Ten days complete deep learning using tenorflow 2.0**


<img src ="https://user-images.githubusercontent.com/52238766/66801842-812d5080-ef55-11e9-916e-cedae5128efe.png">



## :point_right: Requirements

- python 3.6
- tensorflow 2.0 (https://www.tensorflow.org)
- Numpy
- matplotlib
- Anaconda(https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)
- Jupyter Notebook



## :computer: Install

See the [TensorFlow install guide](https://www.tensorflow.org/install) for the
[pip package](https://www.tensorflow.org/install/pip), to
[enable GPU support](https://www.tensorflow.org/install/gpu), use a
[Docker container](https://www.tensorflow.org/install/docker), and
[build from source](https://www.tensorflow.org/install/source).

To install the current release for CPU-only:

```
$ pip install tensorflow
```

Use the GPU package for
[CUDA-enabled GPU cards](https://www.tensorflow.org/install/gpu):

```
$ pip install tensorflow-gpu
```

*Nightly binaries are available for testing using the
[tf-nightly](https://pypi.python.org/pypi/tf-nightly) and
[tf-nightly-gpu](https://pypi.python.org/pypi/tf-nightly-gpu) packages on PyPi.*

#### *Try your first TensorFlow program*

```shell
$ python
```

```python
>>> import tensorflow as tf
>>> tf.enable_eager_execution()
>>> tf.add(1, 2).numpy()
3
>>> hello = tf.constant('Hello, TensorFlow!')
>>> hello.numpy()
'Hello, TensorFlow!'
```

For more examples, see the
[TensorFlow tutorials](https://www.tensorflow.org/tutorials/).



## 📖 Course
#### Day1: Machine Learning 기본
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day1/Day%201.md)
*   [Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day1/Lab01.ipynb)



#### Day2: Linear Regression hypothesis & cost
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day2/Day%202.md)



#### Day3: Linear Regression cost 최적화 알고리즘
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day3/Day%203.md)
*   [Linear regression Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day3/linear%20regression.ipynb)



#### Day4: Multi-variable Linear regression
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day4/Day%204.md)
*   [Multi-variable Linear regression Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day4/Day%204_practice.ipynb)



#### Day5: Logistic Classification & cost function
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day5/Day%205.md)
*   [Logistic Classification Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day5/Day%205_practice.ipynb)



#### Day6: Softmax regression & cost function
*   [Theory](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day6/SoftMax%20Regression.md)
*   [Softmax regression Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day6/SoftmaxAndCostfunction.ipynb)



#### Day7: Rate, Overfitting, Regularization, training & test
*   [Theory 1](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day7/Rate_overfitting_regularization.md)
*   [Theory 2](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day7/Training%26TrainingDataSet.md)
*   [Training & Evaluationn Code](https://github.com/BlueCat-Community/10-Days-Of-DL/blob/master/Day5/Day%205_practice.ipynb)


## :books: Resources

*   [TensorFlow.org](https://www.tensorflow.org)
*   [TensorFlow tutorials](https://www.tensorflow.org/tutorials/)
*   [TensorFlow official models](https://github.com/tensorflow/models/tree/master/official)
*   [TensorFlow examples](https://github.com/tensorflow/examples)
*   [TensorFlow in Practice from Coursera](https://www.coursera.org/specializations/tensorflow-in-practice)
*   [TensorFlow blog](https://blog.tensorflow.org)
*   [TensorFlow Twitter](https://twitter.com/tensorflow)
*   [TensorFlow YouTube](https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ)
*   [TensorFlow roadmap](https://www.tensorflow.org/community/roadmap)
*   [TensorFlow white papers](https://www.tensorflow.org/about/bib)
*   [TensorBoard visualization toolkit](https://github.com/tensorflow/tensorboard)

Learn more about the
[TensorFlow community](https://www.tensorflow.org/community) and how to
[contribute](https://www.tensorflow.org/community/contribute).



## ©️ License
```
 Copyright 2019 Team Daliy_Learning in BlueCat-Community

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```
