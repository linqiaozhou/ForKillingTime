#-*- coding:utf-8 -*-
'''
利用梯度下降算法求解线性回归问题
设线性函数为y=3*x1+4*x2+2.5*x3
'''
import numpy as np
def get_fake_data(sample_num):
    x1=np.linspace(0,10,sample_num)
    x2=np.linspace(10,20,sample_num)
    x3=np.linspace(20,30,sample_num)
    x=np.concatenate(([x1],[x2],[x3]),axis=0).T
    #print x
    y=np.dot(x,np.array([3,4,2.5]).T)
    return x,y

def sgd(sample,label,lr):
    sample_num = sample.shape[0]
    sample_dim = sample.shape[1]
    effc = np.zeros(sample_dim.dtype=np.float)
    deta=np.zeros(sample_dim,dtype=np.float)
    for i in range(sample_num):
        
        
if __name__ == '__main__':
    lr = 0.001
    x,y =get_fake_data(100)
    sgd(x,y,lr)
