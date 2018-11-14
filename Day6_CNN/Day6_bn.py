#coding=uft-8
import numpy as np
import random
class BatchNormal(object):
    def __init__(self,channel):
        self.channel = channel
        self.norm = np.zeros(channel,dtype=float32)
        self.mean = np.zeros(channel,dtype=float32)
        self.variance = np.zeros(channel,dtype=float32)
        self.gammma = np.zeros(channel,dtype=float32)
        self.beta=np.zeros(channel,dtype=float32)
    def forward(self,input_data):
        bath_size,channel,img_h,img_w=input_data.shape
        self.mean = np.mean(input_data,axis=2)
        self.varivance=np.varivance(input_data,axis=2)
        
