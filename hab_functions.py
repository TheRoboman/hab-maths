from math import pi,sqrt,exp,log

# Constants
g = 9.81                # accl due to gravity in m/s^2
R_air = 287.1           # specific gas constant for air in J/kg-K
R_he = 2077.1           # specific gas constant for helium in J/kg-K
T = 250                 # average temperature of atmosphere in K


def Check_Direction(mass_suspended,mass_balloons,volume,rho_air,rho_he):
    # check if net force (without motion/drag) is up or down, and then return the descent flag
    # this function should be run before running the functions to solve for vertical rate or volume
    F = (rho_air-rho_he) * volume * g - (mass_balloons + mass_suspended) * g
    if F > 0:
        descent = False
    else:
        descent = True
    return descent


def Volume_To_Vertical_Rate(volume,Cd,rho_air,rho_he,mass_balloons,mass_suspended,descent):
    mass = mass_balloons + mass_suspended
    radius = ((3*volume)/(4*pi))**(1/3)

    # Group equation terms together for neatness
    a = 8*g*pi*(rho_air-rho_he)*radius**3
    b = -3*Cd*pi*rho_air*radius**2
    c = -6*g*mass

    # Flip the sign of drag term (b) if descending
    if descent:
        b=-b

    vertical_rate = sqrt(a+c/b)
    return vertical_rate


def Vertical_Rate_To_Volume(vertical_rate,Cd,rho_air,rho_he,mass_balloons,mass_suspended,descent):
    mass = mass_balloons + mass_suspended

    # Coefficients of cubic ar^3 + br^2 + cr + d = 0:
    a = 8*g*pi*(rho_air-rho_he)
    b = -3*Cd*pi*rho_air*vertical_rate**2
    c = 0
    d = -6*g*mass

    # Flip the sign of drag term (b) if descending
    if descent:
        b=-b

    # Coefficients of depressed cubic t^3 + pt + q = 0:
    p = (3*a*c-b**2)/(3*a**2)                        # coefficient of depressed cubic t term
    q = (2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)         # coefficient of depressed cubic constant term

    # Solve depressed cubic using Cardano's formula:
    root_t = ((-q / 2) + sqrt((q**2 / 4) + (p**3 / 27)))**(1/3) + ((-q / 2) - sqrt((q**2 / 4) + (p**3 / 27)))**(1/3)
    radius = root_t - (b / (3*a))
    volume = 4/3 * pi * radius**3
    return volume

def Atmospheric_Model(altitude):
# https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html
# https://en.wikipedia.org/wiki/International_Standard_Atmosphere#Description
# The model in this function starts at 0 m AMSL, up to a maximum of 71 km
# Uses SI units (m, K, Pa, kg, J, etc.)

    if (altitude >= 0) and (altitude <= 11000):
        k = 0.0065          # temperature lapse rate (K/m)
        T_base = 288.15     # temperature at base of altitude window in K
        P_base = 101325     # pressure at base of altitude window in Pa
        h_base = 0          # height of base of altitude window in m above sea level
        Temperature = T_base - (k * altitude)
        Pressure = P_base * (1 - (k/T_base) * (altitude - h_base))**(g/(R_air*k))

    elif (altitude > 11000) and (altitude <= 20000):
        k = 0
        T_base = 216.65
        P_base = 22632
        h_base = 11000
        Temperature = T_base
        Pressure = P_base * exp((g/(R_air*T_base)) * (altitude - h_base))

    elif (altitude > 20000) and (altitude <= 32000):
        k = -0.001
        T_base = 216.65
        P_base = 5474.9
        h_base = 20000
        Temperature = T_base - (k * altitude)
        Pressure = P_base * (1 - (k/T_base) * (altitude - h_base))**(g/(R_air*k))

    elif (altitude > 32000) and (altitude <= 47000):
        k = -0.0028
        T_base = 228.65
        P_base = 868.02
        h_base = 32000
        Temperature = T_base - (k * altitude)
        Pressure = P_base * (1 - (k/T_base) * (altitude - h_base))**(g/(R_air*k))

    elif (altitude > 47000) and (altitude <= 51000):
        k = 0
        T_base = 270.65
        P_base = 110.91
        h_base = 47000
        Temperature = T_base
        Pressure = P_base * exp((g/(R_air*T_base)) * (altitude - h_base))

    elif (altitude > 51000) and (altitude <= 71000):
        k = 0.0028
        T_base = 270.65
        P_base = 66.94
        h_base = 51000
        Temperature = T_base - (k * altitude)
        Pressure = P_base * (1 - (k/T_base) * (altitude - h_base))**(g/(R_air*k))

    else:
        print("Altitude must be between 0 - 71 km AMSL")
        return 0,0,0,0

    rho_air = Pressure/(R_air*Temperature)
    rho_he = Pressure/(R_he*Temperature)
    return Temperature,Pressure,rho_air,rho_he


def IdealGasLaw_V(t1,t2,p1,p2,v1):
    # calculate balloon volume at new altitude conditions, where:
    # t1 = old temp, t2 = new temp, p1 = old pressure, p2 = new pressure, v1 = old volume
    v2 = (t2*v1*p1)/(t1*p2)
    return v2


def Neck_Lift_to_Volume(mass_pipe,mass_balloons,neck_lift,rho_air,rho_he):
    mass = mass_pipe + mass_balloons
    volume = (neck_lift + mass)/(rho_air-rho_he)
    return volume


def Volume_to_Neck_Lift(mass_pipe,mass_balloons,volume,rho_air,rho_he):
    mass = mass_pipe + mass_balloons
    neck_lift = volume * (rho_air-rho_he) - mass
    return neck_lift


def simpleBurst_Height(initial_volume,burst_volume):
    burst_height = (R_air * T / g) * log(burst_volume/initial_volume)
    return burst_height


def simpleBurst_Volume(burst_height,burst_volume):
    initial_volume = burst_volume * exp((-g*burst_height)/(R_air*T))
    return initial_volume

        
if __name__ == "__main__":
    pass