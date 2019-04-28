from __future__ import division
import numpy as np
'''-----------------------------------------------------------------------------
Newton diferences class
    Calculates the divided diferences 
    Calculates the polinomial aproximation for a value
-----------------------------------------------------------------------------'''
class NewtonDiferences():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dividedDiferences(self):
        #Calculates all the divided diferences for the list of points
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
        #given a value_to_interpolate aproximates the value through the polinomial
        n = len(a)-1
        tmp = a[n]
        for i in range(1,n+1):
            tmp = tmp*(value_to_interpolate-x[n-i])+a[n-i]
        return tmp
