#coding=utf-8
import numpy as np

class ConvLayer(object):
    def __init__(self,kernel,kernel_num,padding_size,stride):
        self.kernel = kernel
        self.kernel_num=kernel_num
        self.padding_size = padding_size
        self.stride = stride
    def conv2d(self,input_data):
        input_h,input_w = feature.shape
        k_h,k_w=self.kernel.shape
        input_h += 2*self.padding_size
        input_w += 2*self.padding_size
        output_h = input_h/self.stride
        output_w = input_w/self.stride
        padding_input = padding(input_data)
        ret = np.zeros((output_w,output_h),dtype = np.float)
        for h in range(input_h-2*self.padding_size):
            for w in range(input_w-2*self.padding_size):
                temp = padding_input[h:h+k_h,w+w_h]
                ret[h,w]=np.sum(temp*kernel)
        return ret
  def padding(self,input_data):
      org_h,org_w = input_data.shape
      ret = np.zeros((org_h+2*self.padding_size,org_w+self.padding_size),dtype=np.float)
      ret[self.padding_size:org_h+self.padding_size,self.padding_size:org_w+self.padding_size] = input_data
      return ret
  def forward(self,batch_size,input_data):
        
        
      
