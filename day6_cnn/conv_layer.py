#coding=utf-8
import numpy as np

class ConvLayer(object):
    def __init__(self,kernel,kernel_num,padding_size,stride,lr=0.001,momentum=0.9,name="Conv"):
        self.kernel = kernel
        self.kernel_num=kernel_num
        self.padding_size = padding_size
        self.stride = stride
        self.weights =np.random.randn(kernel_num,kernel.shape[0],kernel.shape[1])
        self.bias=np.zeros(kernel_num)
        self.gradient_w = np.zeros_like(self.weights)
        self.gradient_b = np.zeros_like(self.bias)
        self.layer_name =name
        self.lr = lr
        self.momentum =momentum
    def conv2d(self,input_data,kernel,padding=1):
        k_h,k_w=kernel.shape
        if paddding == 1:
            input_data = padding(input_data)
        input_h,input_w = input_data.shape
        output_h = (input_h-k_h+1)/self.stride
        output_w = (input_w-k_w+1)/self.stride
        ret = np.zeros((output_w,output_h),dtype = np.float)
        for h in range(input_h-2*self.padding_size):
            for w in range(input_w-2*self.padding_size):
                temp = input_data[h:h+k_h,w+w_h]
                ret[h,w]=np.sum(temp*kernel)
        return ret
    def padding(self,input_data):
        org_h,org_w = input_data.shape
        ret = np.zeros((org_h+2*self.padding_size,org_w+self.padding_size),dtype=np.float)
        ret[self.padding_size:org_h+self.padding_size,self.padding_size:org_w+self.padding_size] = input_data
        return ret
    def rotate(kernel):
        k_h,k_w=kernel.shape
        ret = np.zeros_like(kernel,dtype=float32)
        for i in range(k_h):
            ret[i,:]=kernel[k_h-i-1,:]
        return ret
        
    def forward(self,batch_size,bottom):
        batch,in_channel,input_h,input_h = bottom.shape
        kernel_num,k_h,kw=self.weights.shape
        output_h = (input_h-k_h)/self.stride+1
        output_w = (input_w-k_w)/self.stride+1
        self.top = np.zeros(batch,kernel_num,k_h,k_w)
        self.bottom =bottom 
        ret = np.zeros((batch,))
        for i in range(batch_size):
            for j in range(kernel_num):
                for k in range(in_channel):
                    self.top[i,j]+=conv2d(bottom[i,k],self.weights[j])
                self.top[i,j]+=self.bias[j]
        return self.top
    #do not can consider the conv with stride and padding exit
    def backward(self,top_diff):
        self.gradient_w = conv2d(self.bottom,top_diff,padding=0)
        self.gradient_b = np.sum(top_diff)
        bottom_diff = conv2d(padding(top_diff),rotate(self.kernel)) #forward padding exit
        return bottom_diff
        
        
          
        
      
