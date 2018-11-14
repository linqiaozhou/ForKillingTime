#coding=utf-8
import numpy as np

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
        for c in range(channel):
            self.mean[c] =np.sum(input_data[:,c,:,:]
        self.mean/=(batch_size*channel*img_h*img_w)
        for c in range(channel):
             self.variance[c] =np.sum((input_data[:,c,:,:]-self.mean[c])**2)
        self.variance /= (batch_size*channel*img_h*img_w)
        for c in range(channel):
            self.norm[:,c,:,:]= (input_data[:,c,:,:]-self.mean[c])/(self.variance[c]+0.0000001)
            output_data[:,c,:,:]= self.norm[:,c,:,:]*self.gamma[c]+self.beta[c]
        return output_data
        
    def backward(self,input_data,residual):
        batch_size,channel,img_h,img_w=residual.shape
        for c in range(channel):
            self.deta_gamma[c] =np.sum(residual[:,c,:,:]*self.norm[:,c,:,:])
            self.deta_beta[c] = np.sum(residual[:,c,:,:])
        deta_norma_x = np.zeros_like(residual,dtype=float32)
        for c in range(channel):
            deta_norma_x[:,c,:,:]=residual[:,c,:,:]*self.gamma[c]
        deta_var = np.zeros(channel,dtype=float32)
        deta_mean = np.zeros(channel,dtype=float32)
        for c in range(channel):
            deta_var[c]=np.sum(deta_norma_x[:,c,:,:]*(input_data[:,c,:,:]-self.mean[c]))
            deta_mean[c] = np.sum(deta_norma_x[:,c,:,:])
        deta_var *= -0.5*(self.variance+0.000001)**(-1.5)                        
        deta_mean *= -1*(self.variance+0.000001)**(-0.5)
        deta_x = np.zeros_like(residual,dtype=float)
        for c in range(channel):
            deta_x[:,c,:,:] = deta_norma_x[:,c,:,:]*(self.variance[c]+0.000001)**(-0.5) \
                              +2*self.variance[c]*(input_data[:,c,:,:]-self.mean[c])/(batch_size*channel*img_h*img_w)\
                              +deta_mean[c]/(batch_size*channel*img_h*img_w)
        return deta_x
