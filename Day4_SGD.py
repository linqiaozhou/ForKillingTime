'''
A simply implementation of  SGD for the classic function :
f(x,y)=(1-x)2+100(y-x2)2
f(1,1) = 0
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
        self.deta_x= -2*(1-self.x)-200*(self.y-self.x*self.x)*(2*self.x)
        return self.deta_x
    def partial_reci_y(self):
        self.deta_y= 200*(self.y-self.x*self.x)
        return  self.deta_y
    def update(self):
        self.x -= self.lr*self.deta_x
        self.y -= self.lr*self.deta_y 
        return
    def obj_fun(self):
        return (1-self.x)**2+100*(self.y-self.x**2)**2
    def cal_loss(self):
        #print self.obj_fun()
        #return pow((0-self.obj_fun()),2)
        return abs(self.obj_fun())
if __name__ == '__main__':
    iter = 0
    lr = 0.0001
    sp_sgd = SGD(0,0,lr)
    while(sp_sgd.cal_loss()>0.001 and iter < 10000):
        iter += 1
        print iter
        print sp_sgd.partial_reci_x()
        print sp_sgd.partial_reci_y()
        sp_sgd.update()
        print sp_sgd.get_xy()
        print sp_sgd.cal_loss()
        #if iter/100.0 == 0.0:
            #print iter,sp_sgd.cal_loss()
    print sp_sgd.cal_loss()
        
    x,y = sp_sgd.get_xy()
    print x,y

