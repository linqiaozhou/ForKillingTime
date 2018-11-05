#coding=utf-8
import numpy as np

class ConvLayer(object):
    def __init__(self,kernel,padding_size,stride):
        self.kernel = kernel
        self.padding_size = padding_size
        self.stride = stride
    def conv2d(self,feature):
        input_h,input_w = feature.shape
        k_h,k_w=self.kernel.shape
        input_h += 2*self.padding_size
        input_w += 2*self.padding_size
        output_h = input_h/self.stride
        output_w = input_w/self.stride
        ret = np.zeros((output_w,output_h),dtype = np.float)
        for h in range(input_h-2*self.padding_size):
            for w in range(input_w-2*self.padding_size):
                for kh in range(k_h):
                    for kw in range(k_w):
                        res[h,w] += feature[h+kh,w+kw]*kernel[kh,kw]
        return ret
  def padding(self,feature):
      org_h,org_w = feature.shape
      np.zeros((org_h+2*self.padding_size,org_w+self.padding_size),dtype=np.float)
      
      
