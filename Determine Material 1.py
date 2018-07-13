from math import pi  
from math import tan
import cmath
x = complex((input('What is XL in form x + jy form? ')))
l = float(input('What is the coefficent of the Length in decimal form? '))
Z0 = complex(input('What is the Characteristic Impedance? '))

a = float(tan((2*pi * l)))

Zin = Z0*((complex(x,a))/(complex(1,x*a)))

print('The complex value in polar {0} (Ohms) and rectangular {1} (Ohms)'.format(cmath.polar(Zin),Zin))
