#-*- coding:utf-8 -*-
'''
利用梯度下降算法求解线性回归问题
设线性函数为y=3*x1+4*x2+5*x3
'''
import numpy as np
def get_fake_data(sample_num):
    x1=np.linspace(0,10,sample_num)
    x2=np.linspace(5,15,sample_num)
    x3=np.linspace(10,20,sample_num)
    x=np.concatenate(([x1],[x2],[x3]),axis=0).T
    y=np.dot(x,np.array([3,4,5]).T)
    return x,y

def sgd(sample,label,lr):
    sample_num,sample_dim = sample.shape
    partial_reci = np.zeros(sample_dim,dtype=np.float)
    coeff=np.zeros(sample_dim,dtype=np.float)
    loss = 100
    iter =0
    while loss > 0.000000001 and iter <100000:
        loss = 0
        iter +=1
        for i in range(sample_num):
            h=np.dot(sample[i],coeff)
            partial_reci+=(h-label[i])*sample[i]
            loss += (h-label[i])**2
        partial_reci /= sample_num
        coeff -= lr*partial_reci
        loss /= 2*sample_num
    return coeff    
if __name__ == '__main__':
    lr = 0.001
    x,y =get_fake_data(100)
    print sgd(x,y,lr)
