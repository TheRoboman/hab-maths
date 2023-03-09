from math import exp, log
import matplotlib.pyplot as plt
import numpy as np


def plotComparison(V_initial):
    T = 250
    R = 287
    g = 9.81


    V0 = V_initial
    T0 = 288.15
    k0 = 0.0065
    power0 = 1-g/(R*k0)

    V1 = V0 * (1 - (k0/T0)*(11000))**power0
    T1 = 216.65

    V2 = V1 * exp(g*9000/(R*T1))
    T2 = 216.65
    k2 = -0.001
    power2 = 1-g/(R*k2)

    V3 = V2 * (1 - (k2/T2)*(12000))**power2
    T3 = 228.65
    k3 = -0.0028
    power3 = 1-g/(R*k3)

    V4 = V3 * (1 - (k3/T3)*(15000))**power3
    T4 = 270.65

    V5 = V4 * exp(g*4000/(R*T4))
    T5 = 270.65
    k5 = 0.0028
    power5 = 1-g/(R*k5)


    x0 = np.linspace(0,11000,11001)
    x1 = np.linspace(0,9000,9001)
    x2 = np.linspace(0,12000,12001)
    x3 = np.linspace(0,15000,15001)
    x4 = np.linspace(0,4000,4001)
    x5 = np.linspace(0,20000,20001)

    # Refined volume functions for each layer of atmosphere
    y0 = V0 * (1 - (k0/T0)*(x0))**power0
    y1 = V1 * np.exp(g*(x1)/(R*T1))
    y2 = V2 * (1 - (k2/T2)*(x2))**power2
    y3 = V3 * (1 - (k3/T3)*(x3))**power3
    y4 = V4 * np.exp(g*(x4)/(R*T4))
    y5 = V5 * (1 - (k5/T5)*(x5))**power5

    # Simple volume function
    z0 = V0 * np.exp(g*(x0)/(R*T))
    z1 = V0 * np.exp(g*(x1+11000)/(R*T))
    z2 = V0 * np.exp(g*(x2+20000)/(R*T))
    z3 = V0 * np.exp(g*(x3+32000)/(R*T))
    z4 = V0 * np.exp(g*(x4+47000)/(R*T))
    z5 = V0 * np.exp(g*(x5+51000)/(R*T))

    # setting the axes at the centre
    fig, axs = plt.subplots(2,3)
    axs[0, 0].plot(x0, y0, 'b')
    axs[0, 0].plot(x0, z0, 'r')
    axs[0, 0].set_title('Troposphere')
    

    axs[0, 1].plot(x1, y1, 'b')
    axs[0, 1].plot(x1, z1, 'r')
    axs[0, 1].set_title('Tropopause')

    axs[0, 2].plot(x2, y2, 'b')
    axs[0, 2].plot(x2, z2, 'r')
    axs[0, 2].set_title('Stratosphere 1')

    axs[1, 0].plot(x3, y3, 'b')
    axs[1, 0].plot(x3, z3, 'r')
    axs[1, 0].set_title('Stratosphere 2')

    axs[1, 1].plot(x4, y4, 'b')
    axs[1, 1].plot(x4, z4, 'r')
    axs[1, 1].set_title('Stratopause')

    axs[1, 2].plot(x5, y5, 'b')
    axs[1, 2].plot(x5, z5, 'r')
    axs[1, 2].set_title('Mesosphere 1')
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()

if __name__ == "__main__":
    # input initial volume V_i in m^3
    V_i = float(input("Enter initial volume in m\u00b3: "))
    # run plotting function with initial volume V_i
    plotComparison(V_i)