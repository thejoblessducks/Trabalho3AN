import numpy as np
import matplotlib.pyplot as plt

import Spline as spl
import Interpolation as inter


f = lambda x: (4*np.power(x,2)+np.sin(9*x))

'''-----------------------------------------------------------------------------
2 A
-----------------------------------------------------------------------------'''
def graphicTable(x_points,y_points):
    data = spl.Spline(x_points,y_points)
    data2 = inter.Interpolation(x_points,y_points)

    data_x,data_y = data.buildSpline()
    data2_x,data2_y= data2.interpolateData()


    plt.plot(x_points,y_points,"o",label="Data")
    plt.plot(data_x,data_y,label="Spline trace")
    plt.plot(data2_x,data2_y,label="Interpolation")
    plt.legend(loc='lower left',ncol=3)
    plt.show()

def graphicTableNatural(x,y):
    data = spl.Spline(x,y)
    data2 = inter.Interpolation(x,y)

    spline = data.buildNormalSpline()
    data2_x,data2_y= data2.interpolateData()
    xs = np.arange(x[0],x[-1]+1,0.00001)



    plt.plot(x,y,"o",label="Data")
    plt.plot(xs,f(xs),label='True Value')
    plt.plot(xs,spline(xs),label="Spline Trace")
    plt.plot(data2_x,data2_y,label="Interpolation")
    plt.legend(loc='lower left',ncol=2)    
    plt.show()

def pointSet(lower,upper,n):
    values = np.linspace(lower,upper,num=n,endpoint=True)
    a = []
    for val in values:
        a.append(f(val))
    return values,np.array(a)

x,y = pointSet(-1,1,10)
'''
x = np.array([0,1,2,2.5,3,4])
y = np.array([1.4,0.6,1.0,0.6,0.6,1.0])
'''
graphicTableNatural(x,y)



