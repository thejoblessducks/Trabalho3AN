import numpy as np
from scipy.interpolate import CubicSpline as cs

'''-----------------------------------------------------------------------------
Class to represent a spline
-----------------------------------------------------------------------------'''
class Spline():
    def __init__(self,x_points,y_points):
        self.x_points = x_points
        self.y_points = y_points
    def buildNormalSpline(self):
        x = self.x_points
        y = self.y_points
        spline = cs(x,y,bc_type='natural')
        return spline
    def showEquations(self,spline=None):
        if not spline:
            spline = self.buildNormalSpline()
        x = self.x_points
        coef = spline.c
        for i in range(len(x)-1):
            val = "{:0.4f}".format(x[i])
            s = "S"+str(i)+"("+val+"<=x<="+"{:0.4f}".format(x[i+1])+") = "
            a = "{:0.4f}".format(coef.item(3,i))
            b = "{:0.4f}".format(coef.item(2,i))
            c = "{:0.4f}".format(coef.item(1,i))
            d = "{:0.4f}".format(coef.item(0,i))
            
            s2 = a+" + "+b+"(x-"+val+") + "+c+"(x-"+val+")^2 + "+d+"(x-"+val+")^3;"
            print( s + s2)
        return
    def calc(self,value,spline=None):
        if not spline:
            spline = self.buildNormalSpline()
        return spline(value)