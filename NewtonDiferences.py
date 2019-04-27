import numpy as np

class NewtonDiferences():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dividedDiferences(self):
        x = self.x
        y = self.y

        n = len(x)
        a = []
        for i in range(n):
            a.append(y[i])
        
        for j in range(1,n):
            for i in range(n-1,j-1,-1):
                a[i] = (a[i]-a[i-1])/(x[i]-x[i-j])
        return np.array(a)
    def calInterpolation(self,a,x,value_to_interpolate):
        n = len(a)-1
        tmp = a[n]
        for i in range(n-1,-1,-1):
            tmp = tmp*(value_to_interpolate-x[i])+a[i]
        return tmp
