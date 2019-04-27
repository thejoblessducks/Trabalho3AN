import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO as gk

plt.ioff()
'''-----------------------------------------------------------------------------
Class to represent a spline
-----------------------------------------------------------------------------'''
class Spline():
    def __init__(self,x_points,y_points):
        self.x_points = x_points
        self.y_points = y_points
    def showData(self):
        x = self.x_points
        y = self.y_points
        plt.plot(x,y,"bo",label="Data")
        plt.show()
    def buildSpline(self):
        lower = self.x_points[0]-1
        upper = self.x_points[-1]+1
        x=self.x_points
        y=self.y_points
        spl = gk() #Build new Model
        spl.x = spl.Param(value=np.linspace(lower,upper))
        spl.y = spl.Var()
        spl.cspline(spl.x,spl.y,x,y)
        spl.options.IMODE = 2
        spl.solve(disp=False) #don't show steps
        return spl.x,spl.y
