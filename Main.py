import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO as gk
import scipy.interpolate as spy

import Spline as spl
import Interpolation as inter


f = lambda x: (4*(x**2)+np.sin(9*x))

'''-----------------------------------------------------------------------------
2 A
-----------------------------------------------------------------------------'''
def graphicTable(x_points,y_points):
    data = spl.Spline(x_points,y_points)
    data2 = inter.Interpolation(x_points,y_points)

    data_x,data_y = data.buildSpline()
    data2_x,data2_y= data2.interpolateData()


    plt.plot(x_points,y_points,"bo",label="Data")
    plt.plot(data_x,data_y,"r--",label="Spline trace")
    #fspline = plt.figure("Spline")


    plt.plot(data2_x,data2_y,"bo",label="Data")
    plt.plot(data2_x,data2_y,"g--",label="Interpolation")
    #finterpolation = plt.figure("Interpolation")
    plt.show()

def pointSet(lower,upper):
    values = np.linspace(lower,upper,10,endpoint=True)
    a = []
    for val in values:
        a.append(f(val))
    return values,np.array(a)

x,y = pointSet(-1,1)

graphicTable(x,y)
'''
x_points = np.array([0,1,2,2.5,3,4])
    y_points = np.array([1.4,0.6,1.0,0.6,0.6,1.0])
    '''
#input("Press any key to close")


