#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:07:01 2017

@author: zxl
"""

import tensorflow as tf

saver = tf.train.Saver()
with tf.Session() as sess:
     sess.run(tf.global_variable_initializer())
     saver.save(sess,"color2gray/tensor_model")
     
saver = tf.train.Saver()
with tf.Session() as sess:
     sess.run(tf.global_variable_initializer())
     saver.save(sess,"color2gray/tensor_model")