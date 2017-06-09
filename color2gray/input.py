#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:28:14 2017

@author: zxl
"""

import os
import tensorflow as tf

filename = os.path.join('data/train','list.txt')
with open(filename) as fid:
    content = fid.read()
content = content.split('\n')
content = content[:-1]
valuequeue = tf.train.string_input_producer(content,shuffle = True)
value = valuequeue.dequeue()
dir,labels = tf.decode_csv(records = value,record_defaults = [["string"],[""]],field_delim = " ")
labels = tf.string_to_number(labels,tf.int32)
imagecontent = tf.read_file(dir)
image = tf.image.decode_png(imagecontent,channels = 3,dtype = tf.uint8)
image = tf.cast(image,tf.float32)
#image = tf.image.resize_images(image,[100,100])
reshape = tf.reshape(tf.reduce_mean(image,[0,1]),[1,1,3] )
#result.uint8image = tf.transpose(image,[1,2,0])
image = image / reshape*128
print "*******input done!*********"

#image = tf.random_crop(image,[IMAGE_SIZE,IMAGE_SIZE,3])
#images,labels_batch = tf.train.shuffle_batch([image,labels],batch_size = batch_size,num_threads = 6,capacity = 3 * batch_size+3000,min_after_dequeue = 3000)
#return images,labels_batch
