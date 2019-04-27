from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar as mn_s


import Spline as spl
import Interpolation as inter


f = lambda x: (4*np.power(x,2)+np.sin(9*x))
f4 = lambda x: 6561*np.cos(9*x)
f11 = lambda x: 31285400229*np.sin(9*x)

def graphicTableNatural(x,y,func=False):
    data = spl.Spline(x,y)
    data2 = inter.Interpolation(x,y)

    spline = data.buildNormalSpline()
    data2_x,data2_y= data2.interpolateData()
    xs = np.arange(x[0],x[-1]+1,0.00001)    

    plt.plot(x,y,"o",label="Data")
    if func:
        plt.plot(xs,f(xs),label='True Value')
    plt.plot(xs,spline(xs),label="Spline Trace")
    plt.plot(data2_x,data2_y,label="Interpolation")
    plt.legend(loc='lower left',ncol=2)
    plt.grid()    
    plt.show()

    return data,spline,data2
def pointSet(lower,upper,n):
    values = np.linspace(lower,upper,num=n,endpoint=True)
    a = []
    for val in values:
        a.append(f(val))
    return values,np.array(a)
    
def maxH(x):
    max_h = None
    for i in range(len(x)-1):
        h = x[i+1]-x[i]
        if not max_h:
            max_h = h
        max_h = max(max_h,h)
    return max_h
def M(lower,upper,interpolation=False):
    if interpolation:
        m = mn_s(lambda x : -f11(x),bounds=[lower,upper],method='bounded')
        return abs(m.x)
    m = mn_s(lambda x : -f4(x),bounds=[lower,upper],method='bounded')
    return abs(m.x)
def interpolationError(x,value,lower,upper):
    m = M(lower,upper,interpolation=True)    
    n1 = len(x)+1
    b = np.arange(1,n1+1)
    fac = b.prod()
    
    mult = 1
    for i in x:
        mult *= (value-i)
    return (m/fac)*mult
def splineError(x,lower,upper):
    m = M(lower,upper,interpolation=False)
    h = maxH(x)
    return (5/384)*m*np.power(h,4)


def ex1():
    x = np.array([0,1,2,2.5,3,4])
    y = np.array([1.4,0.6,1.0,0.6,0.6,1.0])
    graphicTableNatural(x,y,func=False)
def ex2():
    x,y = pointSet(-1,1,10)
    spline,natural, interpolator = graphicTableNatural(x,y,func=True)
    #spline.showEquations(natural)
    print("x=0.3: ")
    print("     S(0.3)="+str(spline.calc(0.3,spline=natural)))
    print("     |f(0.3)-S(0.3)|<="+str(splineError(x,-1,1)))

    print("     p(0.3)="+str(interpolator.calc(0.3)))
    print("     |f(0.3)-p(0.3)<="+str(interpolationError(x,0.3,-1,1)))

    print("\nx=0.83:")
    print("     S(0.83)="+str(spline.calc(0.83,spline=natural)))
    print("     |f(0.83)-S(0.83)|<="+str(splineError(x,-1,1)))

    print("     p(0.3)="+str(interpolator.calc(0.83)))
    print("     |f(0.3)-p(0.3)<="+str(interpolationError(x,0.83,-1,1)))

ex2()




