import numpy as np
import NewtonDiferences as ndiferences
'''-----------------------------------------------------------------------------
Interpolation class
    Calculates the interpolating polinomial using newton method
    Calculates the aproximation of a certain value
-----------------------------------------------------------------------------'''
class Interpolation():
    def __init__(self,x,y):
        self.x = x
        self.y = y #table images of x
        #calculate the list of divided diferences
        newton = ndiferences.NewtonDiferences(x,y)
        divided = newton.dividedDiferences()
        self.divided = divided
        self.newton = newton
    def interpolateData(self):        
        divided = self.divided
        newton = self.newton
        x = self.x
        y = []
        for i in x:
            #calculates the aproximation for each value
            y.append(newton.calInterpolation(divided,x,i))
        y = np.array(y)
        return x,y
    def calc(self,val):
        #given a value of x, val, calculates its aproximation
        divided = self.divided
        newton = self.newton
        x = self.x
        return newton.calInterpolation(divided,x,val)