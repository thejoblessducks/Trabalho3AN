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
    def showEquations(self,spline=None):
        if not spline:
            spline = self.buildNormalSpline()
        x = self.x_points
        y= self.y_points
        coef = spline.c
        for i in range(len(x)-1):
            val = "{:0.4f}".format(x[i])
            s = "S"+str(i)+"("+val+"<=x<="+"{:0.4f}".format(x[i+1])+") = "
            a = "{:0.4f}".format(coef.item(3,i))
            b = "{:0.4f}".format(coef.item(2,i))
            c = "{:0.4f}".format(coef.item(1,i))
            d = "{:0.4f}".format(coef.item(0,i))
            s2 = str(a)+" + "+b+"(x-"+val+") + "+c+"(x-"+val+")^2 + "+d+"(x-"+val+")^3;"
            print( s + s2)
        return
