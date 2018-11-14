#coding=uft-8
import numpy as np
import random
class BatchNormal(object):
    def __init__(self,channel):
        self.channel = channel
        self.norm = np.zeros(channel,dtype=float32)
        self.mean = np.zeros(channel,dtype=float32)
        self.variance = np.zeros(channel,dtype=float32)
        self.gammma = np.random.randn(channel,dtype=float32)
        self.beta=np.random.randn(channel,dtype=float32)
    def forward(self,input_data):
        batch_size,channel,img_h,img_w=input_data.shape
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.mean[c] += input_data[b,c,h,w]
        self.mean/=input_data.size
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.variance[c] += (input_data[b,c,h,w]-self.mean[c])**2
        self.variance /= input_data.size
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.norm[b,c,h,w]= (input_data[b,c,h,w]-self.mean[c])/(self.variance[c]+0.0000001)
                        
        
        
