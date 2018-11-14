#coding=uft-8
import numpy as np
import random
class BatchNormal(object):
    def __init__(self,input_data):
        batch_size,channel,img_h,img_w=input_data.shape
        self.channel = channel
        self.norm = np.zeros_like(input_data,dtype=float32)
        self.mean = np.zeros(channel,dtype=float32)
        self.variance = np.zeros(channel,dtype=float32)
        self.gammma = np.random.randn(channel,dtype=float32)
        self.beta=np.random.randn(channel,dtype=float32)
        self.deta_gama=np.zeros(channel,dtype=float32)
        self.deta_beta=np.zeros(channel,dtype=float32)
    def forward(self,input_data):
        batch_size,channel,img_h,img_w=input_data.shape
        output_data = np.zeros_like(input_data,dtype=float32)
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.mean[c] += input_data[b,c,h,w]
        self.mean/=(batch_size*channel*img_h*img_w)
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.variance[c] += (input_data[b,c,h,w]-self.mean[c])**2
        self.variance /= (batch_size*channel*img_h*img_w)
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.norm[b,c,h,w]= (input_data[b,c,h,w]-self.mean[c])/(self.variance[c]+0.0000001)
                        output_data[b,c,h,w]= self.norm[b,c,h,w]*self.gamma[c]+self.beta[c]
        return output_data
        
    def backward(self,input_data,residual):
        batch_size,channel,img_h,img_w=residual.shape
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        self.deta_gamma[c] += residual[b,c,h,w]*self.norm[b,c,h,w]
                        self.deta_beta[c] += residual[b,c,h,w]
        deta_norma_x = np.zeros_like(residual,dtype=float32)
        for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        deta_norma_x [b,c,h,w]=residual[b,c,h,w]*self.gamma[c]
         deta_var = np.zeros(channel,dtype=float32)
         deta_mean = np.zeros(channel,dtype=float32)
         for b in range(batch_size):
            for c in range(channel):
                for h in range(img_h):
                    for w in range(img_w):
                        deta_var[c]+=deta_norma_x[b,c,h,w]*(input_data[b,c,h,w]-self.mean[c])
                        deta_mean[c] +=  deta_norma_x[b,c,h,w]   
         deta_var *= -0.5*(self.variance+0.000001)**(-1.5)                        
         deta_mean *= -1*(self.variance+0.000001)**(-0.5)
