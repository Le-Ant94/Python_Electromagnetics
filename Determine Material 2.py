#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Anthony Le

Program 2: Determine if a material is a Lossless Medium, a Low-Loss Medium, a Good Conductor,
or Any Medium.  Then, calculate the propagation parameters.

"""

from math import pi
from math import sqrt



def Deter_Medium():
    
    if q == 0:
        
        print("\nThe material is a Lossless Medium")
        
        Calc_Lossless()
        
    elif (q/(w*er*8.854*10**-12)) < 0.01:
        
        print("\nThe material is a Low-Loss Medium")
        
        Calc_LowLoss()
        
    elif (q/(w*er*8.854*10**-12)) > 100:
        
        print("\nThe material is a Good Conducting Medium")
        
        Calc_Good()
        
    else:
        
        print("\nThe material is Any Medium")

        Calc_Any()



def Calc_Lossless():
    
    a = 0
    B = w*sqrt((ur*4*pi*10**-7)*(er*8.854*10**-12))
    nc = sqrt((ur*4*pi*10**-7)/(er*8.854*10**-12))
    up = 1/sqrt((ur*4*pi*10**-7)*(er*8.854*10**-12))
    l = up/(w/(2*pi))
    
    print("\nThe attenuation constant (a) is: ", a, " (Np/m)")
    print("\nThe phase constant (B) is: ", B, " (rad/m)")
    print("\nThe characteristic wave impedance (nc) is: ", nc, " (Ω)")
    print("\nThe phase velocity (up) is: ", up, " (m/s)")
    print("\nThe wavelength (l) is: ", l, " (m)")
    print("\nThe skin depth (ds) is undefined")
    
    

def Calc_LowLoss():
    
    a = (q/2)*sqrt((ur*4*pi*10**-7)/(er*8.854*10**-12))
    B = w*sqrt((ur*4*pi*10**-7)*(er*8.854*10**-12))
    nc = sqrt((ur*4*pi*10**-7)/(er*8.854*10**-12))
    up = 1/sqrt((ur*4*pi*10**-7)*(er*8.854*10**-12))
    l = up/(w/(2*pi))
    ds = 1/a
    
    print("\nThe attenuation constant (a) is: ", a, " (Np/m)")
    print("\nThe phase constant (B) is: ", B, " (rad/m)")
    print("\nThe characteristic wave impedance (nc) is: ", nc, " (Ω)")
    print("\nThe phase velocity (up) is: ", up, " (m/s)")
    print("\nThe wavelength (l) is: ", l, " (m)")
    print("\nThe skin depth (ds) is: ", ds, " (m)")

    
    
def Calc_Good():
    
    a = sqrt(pi*(w/(2*pi))*(ur*4*pi*10**-7)*q)
    B = a
    nc = complex(a/q, a/q)
    up = sqrt((4*pi*(w/(2*pi)))/((ur*4*pi*10**-7)*q))
    l = up/(w/(2*pi))
    ds = 1/a
    
    print("\nThe attenuation constant (a) is: ", a, " (Np/m)")
    print("\nThe phase constant (B) is: ", B, " (rad/m)")
    print("\nThe characteristic wave impedance (nc) is: ", nc, " (Ω)")
    print("\nThe phase velocity (up) is: ", up, " (m/s)")
    print("\nThe wavelength (l) is: ", l, " (m)")
    print("\nThe skin depth (ds) is: ", ds, " (m)")
    
    

def Calc_Any():
    
    a = w*sqrt(((ur*4*pi*10**-7*er*8.854*10**-12)/2)*(sqrt(1+(q/(w*er*8.854*10**-12))**2)-1))
    B = w*sqrt(((ur*4*pi*10**-7*er*8.854*10**-12)/2)*(sqrt(1+(q/(w*er*8.854*10**-12))**2)+1))
    nc = (sqrt((ur*4*pi*10**-7)/(er*8.854*10**-12)))*(complex(1, -q/(w*er*8.854*10**-12)))**-0.5
    up = w/B
    l = (2*pi)/B
    ds = 1/a
    
    print("\nThe attenuation constant (a) is: ", a, " (Np/m)")
    print("\nThe phase constant (B) is: ", B, " (rad/m)")
    print("\nThe characteristic wave impedance (nc) is: ", nc, " (Ω)")
    print("\nThe phase velocity (up) is: ", up, " (m/s)")
    print("\nThe wavelength (l) is: ", l, " (m)")
    print("\nThe skin depth (ds) is: ", ds, " (m)")



def main():
    
    choice = True
    
    while choice:
    
        print("""
                      Select a material from the chart:

                            Material Properties

Choices   Materials                 er                q (S/m)              ur
                  
1         Air                       1                 5E-15                1.00000037
2         Fresh water               80                5E-4                 0.999992
3         Sea water                 80                3                    1
4         Ice                       3.5               1E-5                 1
5         Clay                      20                5                    1  
6         Saturated Sand            30                1E-4                 1
7         Barium Titanate           3279              1E-6                 1
8         Cold rolled steel         1                 1E7                  1E2
9         Purified iron             1                 1E7                  5E3
10        Mu metal                  1                 1.6E6                2E5
11        2-81 Permalloy            1                 1E2                  1E6
12        Copper                    1                 5.96E7               0.999994
13        Gold                      1                 4.1E7                1
14        Aluminum                  1                 3.5E7                1.000022
15        Tungsten                  1                 1.79E7               1
16        Graphite                  12.5              2E5                  1
17        Diamond                   7.5               1E-13                0.99999975
18        Silicon                   11.68             1.56E-3              1
19        Glass                     65                1E-15                1
20        Wood - Kiln Dried         4                 1E-15                1.00000043
21        PTFE                      2.1               1E-25                1
""")

        
        choice = int(input("\nChoice of material: "))

        if choice == 1:
            
            global er, q, ur, w, a, B, nc, up, l, ds
            
            er = 1
            q = 5*10**-15
            ur = 1.00000037
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
            
            break;
            
        elif choice == 2:
            
            er = 80
            q = 5*10**-4
            ur = 0.999992
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 3:
            
            er = 80
            q = 3
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 4:
            
            er = 3.5
            q = 1*10**-5
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 5:
            
            er = 20
            q = 5
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 6:
            
            er = 30
            q = 1*10**-4
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 7:
            
            er = 3279
            q = 1*10**-6
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 8:
            
            er = 1
            q = 1*10**7
            ur = 100
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 9:
            
            er = 1
            q = 1*10**7
            ur = 5*10**3
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 10:
            
            er = 1
            q = 1.6*10**6
            ur = 2*10**5
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 11:
            
            er = 1
            q = 100
            ur = 1*10**6
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 12:
            
            er = 1
            q = 5.96*10**7
            ur = 0.999994
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 13:
            
            er = 1
            q = 4.1*10**7
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 14:
            
            er = 1
            q = 3.5*10**7
            ur = 1.000022
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 15:
            
            er = 1
            q = 1.79*10**7
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 16:
            
            er = 12.5
            q = 2*10**5
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 17:
            
            er = 7.5
            q = 1*10**-13
            ur = 0.99999975
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 18:
            
            er = 11.68
            q = 1.56*10**-3
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 19:
            
            er = 65
            q = 1*10**-15
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 20:
            
            er = 4
            q = 1*10**-15
            ur = 1.00000043
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        elif choice == 21:
            
            er = 2.1
            q = 1*10*-25
            ur = 1
            
            print("\nInput value for w in Hz:")
            w = float(input("\nw = "))
            
            Deter_Medium()
        
            break;
        
        else:
            
            x = input("\nInvalid choice. Try again? Y or N ")
            
            if (x == "N") or (x == "n"):
                
                break;
      
        
        
main()
