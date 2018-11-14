#coding=utf-8

import numpy as np
class NetWork(object):
    def __init__(self,laye_sizes):
        self.layer_nums = len(layer_sizes)
        #每一层的神经元的个数，如[1,2,3]
        self.layer_sizes = layer_sizes
        self.bias = [np.random.randn(y,1) for y in layer_sizes[1:]]
        self.weights = [np.random.randn(y,x) \
                        for x,y in zip(layer_sizes[:-1],layer_sizes[1:])]
        self.deta_bias = np.zeros(self.bias.shape,dtype=np.float)
        self.deta_weights = np.zeros(self.weights.shape,dtype=np.float)
        self.activations = np.zeros(self.hidden_layers.shape,dtype = np.float)
    def forward(self,input_data):
        index = 0
        for w,b in zip(self.weights,self.bias):
            self.hidden_layers[index]= np.dot(w, input_data.T)+b
            input_data= sigmoid(self.hidden_layers[index])
            self.activations[index] = input_data
            index +=1
        return input_data
    def backward(self,data_label):
        activation = self.activation[-1]
        erro = (activation-y)*sigmoid_deriv(activation)
        self.deta_bias[-1] = erro
        self.deta_weights[-1] = np.dot(erro.T,self.activation[-2])
        for layer_id in range(2,self.layer_nums):
            erro = np.dot(self.deta_weights[-layer_id+1].T,erro)*sigmoid(self.activation[-layer_id])
            self.deta_bias[-layer_id]=erro
            self.deta_weights[-layer]=np.dot(erro.T,self.activation[-layer_id-1])
    def update(self,learning_rate):
        for layer_id in range(self.layer_nums):
            self.weights[layer_id] -= learing_rate*self.deta_weights[layer_id]
            self.bias[layer_id] -= learing_rate*self.deta_bias[layer_id]
            
    def sgd(self,train_data,epoch,learning_rate,test_data=None):
        iter = 0
        data,label=train_data
        if iter < epoch:
            index= 0
            for index in range(len(label)):
                forward(data[index])
                backward(label[index])
                update(learning_rate)    
    @staticmethod
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))
    @staticmethod
    def sigmoid_deriv(z):
        return sigmoid(z)*(1-sigoid(z))
    
        
def demo():
    
    pass

if __name__ == '__main__':
    demo()
    
    
        
    
