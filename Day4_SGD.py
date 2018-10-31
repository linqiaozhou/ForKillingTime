'''
A simply implementation of  SGD for the classic function :
f(x,y)=(1-x)2+100(y-x2)2
'''
from math import *
class SGD:
    def __init__(self,x,y,lr):
        self.lr = lr
        self.x = x
        self.y = y
        self.deta_x = 0
        self.deta_y = 0
    def get_xy(self):
        return self.x,self.y
    def partial_reci_x(self):
        self.deta_x= -2*self.x-200*(self.y-self.x*self.x)*(-2*self.x)
    def partial_reci_y(self):
        self.deta_y= 200*(self.y-self.x*self.x)
    def update(self):
        self.x -= self.lr*self.deta_x
        self.y -= self.lr*self.deta_y 
        return
    def obj_fun(x,y):
        return pow(1-x,2)+100*pow((y-pow(x,2)),2)
    def cal_loss(self):
        return pow((0-obj_fun(self.x,self.y)),2)
if __name__ == '__main__':
    iter = 0
    lr = 0.1
    sp_sgd = SGD(0,0,0.1)
    while(sp_sgd.cal_loss>1 or iter > 10000):
        iter += 1
        sp_sgd.partial_reci_x()
        sp_sgd.partial_reci_y()
        sp_sgd.update()
    print sp_sgd.loss()
        
    x,y = sp.sgd.get_xy()
    print x,y

