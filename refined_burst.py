from math import exp, log
from hab_functions import simpleBurst_Height

R = 287
g = 9.81

def isothermalFunction_h(T,V,V_base):
    h = (R*T/g) * log(V/V_base)
    return h

def isothermalFunction_V(T,h,V_base):
    V = V_base * exp(g*h/(R*T))
    return V

def nonisothermalFunction_h(k,T_base,V,V_base):
    h = (T_base/k) * (1-(V/V_base)**(1/(1-(g/(R*k)))))
    return h

def nonisothermalFunction_V(k,T_base,h,V_base):
    V = V_base*(1-(k*h/T_base))**(1-g/(R*k))
    return V

def refinedBurst_Height(V_initial,V_burst):
    # Ensure initial volume is less than burst volume before continuing
    if V_initial > V_burst:
        print("Initial volume must be < burst volume!")
        return -1
    elif V_initial == V_burst:
        print("Burst at 0 m ASL")
        return 0
    
    # Check for burst in troposphere:
    V_0 = V_initial
    H_lower = 0
    H_upper = 11000
    h_max = H_upper - H_lower
    k = 0.0065
    T_base = 288.15

    V_1 = nonisothermalFunction_V(k,T_base,h_max,V_0)
    if V_1 == V_burst:
        h_burst = h_max
        return (H_lower+h_burst)
    elif V_1 > V_burst:
        h_burst = nonisothermalFunction_h(k,T_base,V_burst,V_0)
        return (H_lower+h_burst)

    # Check for burst in tropopause:
    H_lower = 11000
    H_upper = 20000
    h_max = H_upper - H_lower
    T_base = 216.65

    V_2 = isothermalFunction_V(T_base,h_max,V_1)
    if V_2 == V_burst:
        h_burst = h_max
        return (H_lower+h_burst)
    elif V_2 > V_burst:
        h_burst = isothermalFunction_h(T_base,V_burst,V_1)
        return (H_lower+h_burst)

    # Check for burst in stratosphere 1:
    H_lower = 20000
    H_upper = 32000
    h_max = H_upper - H_lower
    k = -0.001
    T_base = 216.65

    V_3 = nonisothermalFunction_V(k,T_base,h_max,V_2)
    if V_3 == V_burst:
        h_burst = h_max
        return (H_lower+h_burst)
    elif V_3 > V_burst:
        h_burst = nonisothermalFunction_h(k,T_base,V_burst,V_2)
        return (H_lower+h_burst)

    # Check for burst in stratosphere 2:
    H_lower = 32000
    H_upper = 47000
    h_max = H_upper - H_lower
    k = -0.0028
    T_base = 228.65

    V_4 = nonisothermalFunction_V(k,T_base,h_max,V_3)
    if V_4 == V_burst:
        h_burst = h_max
        return (H_lower+h_burst)
    elif V_4 > V_burst:
        h_burst = nonisothermalFunction_h(k,T_base,V_burst,V_3)
        return (H_lower+h_burst)

    # Check for burst in stratopause:
    H_lower = 47000
    H_upper = 51000
    h_max = H_upper - H_lower
    T_base = 270.65

    V_5 = isothermalFunction_V(T_base,h_max,V_4)
    if V_5 == V_burst:
        h_burst = h_max
        return (H_lower+h_burst)
    elif V_5 > V_burst:
        h_burst = isothermalFunction_h(T_base,V_burst,V_4)
        return (H_lower+h_burst)

    # Return 
    print("Burst altitude outside range 0 - 51 km.")
    return -2

if __name__ == "__main__":
    V_i = float(input("Enter initial volume in m\u00b3: "))
    V_b = float(input("Enter burst volume in m\u00b3: "))
    H_b = refinedBurst_Height(V_i,V_b)
    print(f"Refined burst height is {H_b:.2f} m\u00b3")
    H_sb = simpleBurst_Height(V_i,V_b)
    print(f"Simple burst height is {H_sb:.2f} m\u00b3")
