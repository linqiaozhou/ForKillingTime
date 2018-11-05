#coding=utf-8
import numpy as np

class ConvLayar(object):
  def conv2d(feature,kernel,padding = 0,stride=1):
    input_h,input_w = feature.shape
    input_h += 2*padding
    input_w += 2*padding
    k_h,k_w=kernel.shape
    output_h = input_h /stride
    output_w = input_w/stride
    ret = np.zeros((output_w,output_h),dtype = np.float)
    for h in range(input_h):
        for w in range(input_w):
    
