import numpy as np
import NewtonDiferences as ndiferences

class Interpolation():
    def __init__(self,x,y):
        self.x = x
        self.y = y
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
            y.append(newton.calInterpolation(divided,x,i))
        y = np.array(y)
        return x,y
    def calc(self,val):
        divided = self.divided
        newton = self.newton
        x = self.x
        return newton.calInterpolation(divided,x,val)