# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:56:44 2018

@author: lijun
"""
"""
This model is based on Tensorflow-1.14.
How to use? out1,out2=CRMSS(img1,img2,reuse=False)
img1 and img2 are inputs that are nomalized between 0~1.
out1 and out2 are corresponding cloud removal results for img1 and img2.
If you use this code for your research, please cite us accordingly:
Li, J., Wu, Z.C., Hu, Z.W., Li Z.L., Wang, Y.S., Molinier, M., 2021. Deep learning based thin cloud removal fusing vegetation red edge and short wave infrared spectral information for Sentinel-2A imagery. Remote Sens. 13(1), 157.
"""
import tensorflow as tf
def make_var(name, shape, trainable = True):
    return tf.get_variable(name, shape, trainable = trainable)
 
def conv2d(input_, output_dim, kernel_size=3, stride=2, padding = "SAME", name = "conv2d", biased = False):
    input_dim = input_.get_shape()[-1]
    with tf.variable_scope(name):
        kernel = make_var(name = 'weights', shape=[kernel_size, kernel_size, input_dim, output_dim])
        output = tf.nn.conv2d(input_, kernel, [1, stride, stride, 1], padding = padding)
        if biased:
            biases = make_var(name = 'biases', shape = [output_dim])
            output = tf.nn.bias_add(output, biases)
        return output     
def deconv2d(input_, output_dim, kernel_size=4, stride=2, padding = "SAME", name = "deconv2d"):
    input_dim = input_.get_shape()[-1]
    batchsize=int(input_.get_shape()[0])
    input_height = int(input_.get_shape()[1])
    input_width = int(input_.get_shape()[2])
    with tf.variable_scope(name):
        kernel = make_var(name = 'weights', shape = [kernel_size, kernel_size, output_dim, input_dim])
        output = tf.nn.conv2d_transpose(input_, kernel, [batchsize, input_height * stride, input_width * stride, output_dim], [1, 2, 2, 1], padding = "SAME")
        return output
def instance_norms(input_, name="instance_norm"):
    return tf.contrib.layers.instance_norm(input_,scope=name)
def lrelu(x, leak=0.2, name = "lrelu"):
    return tf.maximum(x, leak*x)


def CRMSS(image,image1, gf_dim=64, reuse=False, name="generator"):
    output_dim=image.get_shape()[-1]
    output_dim1 = image1.get_shape()[-1]
    with tf.variable_scope(name):
        # image is 256 x 256 x input_c_dim
        if reuse:
            tf.get_variable_scope().reuse_variables()
        else:
            assert tf.get_variable_scope().reuse is False

        e1 = lrelu(conv2d(image, gf_dim,stride=1, name='g_e1_conv'))       
        e0 = lrelu(conv2d(image1, gf_dim,stride=1, name='g_e0_conv'))      
        e2 = lrelu(instance_norm(conv2d(e1, gf_dim*2, name='g_e2_conv'), 'g_bn_e2'))
        e20= tf.concat([e2,e0],axis=3)  
        e3 = lrelu(instance_norm(conv2d(e20, gf_dim*4, name='g_e3_conv'), 'g_bn_e3'))
        e4 = lrelu(instance_norm(conv2d(e3, gf_dim*8, name='g_e4_conv'), 'g_bn_e4'))
        e5 = lrelu(instance_norm(conv2d(e4, gf_dim*8, name='g_e5_conv'), 'g_bn_e5'))
        e6 = lrelu(instance_norm(conv2d(e5, gf_dim*8, name='g_e6_conv'), 'g_bn_e6'))
                      
        d1 = relu(instance_norm(deconv2d(e6, gf_dim*8, name='g_d1'),'d_bn_d0'))
        d1 = tf.concat([d1, e5],3)

        d2 = relu(instance_norm(deconv2d(d1, gf_dim*8, name='g_d2'),'g_bn_d1'))
        d2 = tf.concat([d2,e4], 3)

        d3 = relu(instance_norm(deconv2d(d2, gf_dim*4, name='g_d3'),'g_bn_d2'))
        d3 = tf.concat([d3, e3], 3)

        d4 = relu(instance_norm(deconv2d(d3, gf_dim*2, name='g_d4'),'g_bn_d3'))
        d4 = tf.concat([d4,e20], 3)

        d5 = relu(instance_norm(deconv2d(d4, gf_dim, name='g_d5'),'g_bn_d4'))
        d5 = tf.concat([d5,e1], 3)
        
        out1 = conv2d(d4,output_dim1,stride=1, name='out1_conv')       

        out = conv2d(d5,output_dim,stride=1,  name='out_conv')

        return tf.nn.sigmoid(out),tf.nn.sigmoid(out1)
