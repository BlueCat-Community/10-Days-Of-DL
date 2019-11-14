import tensorflow as tf

# simple way
w = tf.Variable(tf.initializers.glorot_uniform()(shape=[784,256]))
#get_variable changed to Variable as tensorflow upgraded into 2.0
#initializer=tf.contrib.layers.xavier_initializer() changed to tf.initializers.glorot_uniform
#as tensorflow upgraded into 2.0

#inside
#input place holders
tf.compat.v1.disable_eager_execution()
#this code is added to disable the default activate eager execution as tensorflow is upgraded into 2.0
X = tf.compat.v1.placeholder(tf.float32, [None,784])
y = tf.compat.v1.placeholder(tf.float32,[None,10])
#tf.placeholder is changed to tf.compat.v1.placeholder as tensorflow upgraded into 2.0

#weights & bias for nn layers
#code from http://stackoverflow.com/questions/33640581 as tensorflow 2.0
W1 = tf.Variable(tf.initializers.glorot_uniform()(shape=[784,256]))
#get_variable changed to Variable as tensorflow upgraded into 2.0
#initializer=tf.contrib.layers.xavier_initializer() changed to tf.initializers.glorot_uniform
#as tensorflow upgraded into 2.0
b1 = tf.Variable(tf.random.normal([256]))
#tf.random_normal changed into tf.random.normal as tensorflow upgraded into 2.0
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)

W2 = tf.Variable(tf.initializers.glorot_uniform()(shape=[256,256]))
#get_variable changed to Variable as tensorflow upgraded into 2.0
#initializer=tf.contrib.layers.xavier_initializer() changed to tf.initializers.glorot_uniform
#as tensorflow upgraded into 2.0
b2 = tf.Variable(tf.random.normal([256]))
#tf.random_normal changed into tf.random.normal as tensorflow upgraded into 2.0
L2 = tf.nn.relu(tf.matmul(L1,W2)+b2)

W3 = tf.Variable(tf.initializers.glorot_uniform()(shape=[256,10]))
#get_variable changed to Variable as tensorflow upgraded into 2.0
#initializer=tf.contrib.layers.xavier_initializer() changed to tf.initializers.glorot_uniform
#as tensorflow upgraded into 2.0
b3 = tf.Variable(tf.random.normal([10]))
#tf.random_normal changed into tf.random.normal as tensorflow upgraded into 2.0
L3 = tf.nn.relu(tf.matmul(L2,W3)+b3)

#define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)