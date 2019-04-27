import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO as gk
from scipy.interpolate import CubicSpline as cs

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
        #The spline is not a natural spline
        lower = self.x_points[0]
        upper = self.x_points[-1]
        x=self.x_points
        y=self.y_points
        spl = gk() #Build new Model
        spl.x = spl.Param(value=np.linspace(lower,upper))
        spl.y = spl.Var()
        spl.cspline(spl.x,spl.y,x,y)
        spl.options.IMODE = 2
        spl.solve(disp=False) #don't show steps
        return spl.x,spl.y
    def buildNormalSpline(self):
        x = self.x_points
        y = self.y_points
        spline = cs(x,y,bc_type='natural')
        return spline
