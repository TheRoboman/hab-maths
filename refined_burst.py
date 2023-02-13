from math import exp, log
import matplotlib.pyplot as plt
import numpy as np

def plotSection1():

    R = 287
    T = 250
    g = 9.81

    T0 = 288.19
    k0 = 0.00652
    power0 = 1-g/(R*k0)

    # 100 linearly spaced numbers
    x = np.linspace(0,11000,11001)

    # the functions
    y = np.exp(g*x/(R*T))
    z = (1 - (k0/T0)*x)**power0

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r')
    plt.plot(x,z, 'b')

    # show the plot
    plt.show()

def plotSection2():

    R = 287
    T = 250
    g = 9.81

    T0 = 288.19
    k0 = 0.00652
    power0 = 1-g/(R*k0)

    T1 = 216.65

    # 100 linearly spaced numbers
    x = np.linspace(11000,20000,9001)\

    # the functions
    y = np.exp(-g*x/(R*T))
    z = np.exp(-g*(x-11000)/(R*T1))*(1 - (k0/T0)*(11000))**-power0

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r')
    plt.plot(x,z, 'b')

    # show the plot
    plt.show()


def isothermalFunction_h(T,V_burst,V_base):
    R = 287
    g = 9.81
    h = (R*T/g) * log(V_burst/V_base)

def isothermalFunction_V(T,V_burst,V_base):
    R = 287
    g = 9.81
    h = (R*T/g) * log(V_burst/V_base)

def nonisothermalFunction_h(k,T,V_burst,V_base):
    R = 287
    g = 9.81
    h = (T/k) * (1-(V_burst/V_base)^(1/(1-(g/(R*k)))))

def nonisothermalFunction_V(k,T,V_burst,V_base):
    R = 287
    g = 9.81
    h = (T/k) * (1-(V_burst/V_base)^(1/(1-(g/(R*k)))))

def testBurstHeights(V_burst,V_base):
    # Check for burst in tropopause:
    h = nonisothermalFunction_h(0.0065,288.15,V_burst,V_base)
    if 


if __name__ == "__main__":
    plotSection2()