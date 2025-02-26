import tensorflow as tf
tf.compat.v1.disable_v2_behavior() 
import numpy as np
import tf_slim as slim  

def resblock(inputs, out_channel=32, name='resblock'):
    with tf.compat.v1.variable_scope(name):  # Corregido para TF 2.x
        x = slim.conv2d(inputs, out_channel, [3, 3], activation_fn=None, scope='conv1')
        x = tf.nn.leaky_relu(x)
        x = slim.conv2d(x, out_channel, [3, 3], activation_fn=None, scope='conv2')
        return x + inputs

def unet_generator(inputs, channel=32, num_blocks=4, name='generator', reuse=True):
    with tf.compat.v1.variable_scope(name, reuse=tf.compat.v1.AUTO_REUSE):  # Corregido
        x0 = slim.conv2d(inputs, channel, [7, 7], activation_fn=None)
        x0 = tf.nn.leaky_relu(x0)
        
        x1 = slim.conv2d(x0, channel, [3, 3], stride=2, activation_fn=None)
        x1 = tf.nn.leaky_relu(x1)
        x1 = slim.conv2d(x1, channel*2, [3, 3], activation_fn=None)
        x1 = tf.nn.leaky_relu(x1)
        
        x2 = slim.conv2d(x1, channel*2, [3, 3], stride=2, activation_fn=None)
        x2 = tf.nn.leaky_relu(x2)
        x2 = slim.conv2d(x2, channel*4, [3, 3], activation_fn=None)
        x2 = tf.nn.leaky_relu(x2)
        
        for idx in range(num_blocks):
            x2 = resblock(x2, out_channel=channel*4, name=f'block_{idx}')  # f-string compatible
            
        x2 = slim.conv2d(x2, channel*2, [3, 3], activation_fn=None)
        x2 = tf.nn.leaky_relu(x2)
        
        # Corrección de redimensionamiento para TF 2.x
        h1, w1 = tf.shape(x2)[1], tf.shape(x2)[2]
        x3 = tf.image.resize(x2, (h1*2, w1*2), method=tf.image.ResizeMethod.BILINEAR)
        x3 = slim.conv2d(x3 + x1, channel*2, [3, 3], activation_fn=None)
        x3 = tf.nn.leaky_relu(x3)
        x3 = slim.conv2d(x3, channel, [3, 3], activation_fn=None)
        x3 = tf.nn.leaky_relu(x3)
        
        h2, w2 = tf.shape(x3)[1], tf.shape(x3)[2]
        x4 = tf.image.resize(x3, (h2*2, w2*2), method=tf.image.ResizeMethod.BILINEAR)
        x4 = slim.conv2d(x4 + x0, channel, [3, 3], activation_fn=None)
        x4 = tf.nn.leaky_relu(x4)
        x4 = slim.conv2d(x4, 3, [7, 7], activation_fn=None)
        
        return x4