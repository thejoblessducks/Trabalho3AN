import numpy as np
import matplotlib.pyplot as plt
import NewtonDiferences as ndiferences

plt.ioff()
class Interpolation():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        newton = ndiferences.NewtonDiferences(x,y)
        divided = newton.dividedDiferences()
        self.divided = divided
        self.newton = newton
    def interpolateData(self):        
        initial = self.x[0]
        end = self.x[-1]
        divided = self.divided
        newton = self.newton

        n = len(self.x)
        x = self.x
        '''x = []
        for i in range(n):
            x.append(i)
        x = np.array(x)'''

        y = []
        for i in x:
            y.append(newton.calInterpolation(divided,x,i))
        y = np.array(y)
        return x,y