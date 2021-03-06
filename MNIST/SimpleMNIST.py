# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:53:10 2018
简单的手写数字识别
@author: 常雪峰
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import  input_data

mnist = input_data.read_data_sets('MNIST_data',one_hot=True) 
# 训练批次大小
batch_size = 100
#计算批次数
n_batch = mnist.train.num_examples//batch_size
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#创建一个简单的神经网络
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros(10))
prediction = tf.nn.softmax(tf.matmul(x,W)+b)

Loss = tf.reduce_mean(tf.square(y-prediction))

train_step = tf.train.GradientDescentOptimizer(0.2).minimize(Loss)
init = tf.global_variables_initializer()
correct_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict = {x:batch_xs,y:batch_ys})
        
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print('Iter'+str(epoch)+'Testing acc'+str(acc))