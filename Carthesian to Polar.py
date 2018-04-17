from math import sqrt, atan2,atan,atanh,tan,degrees

__author__ = 'Razvan'


Xcoordinate= float(input("Give a X coordinate :"))
Ycoordinate= float(input("Give a Y coordinate :"))


Theta= atan(Ycoordinate/Xcoordinate)

Radius =sqrt(Xcoordinate**2+Ycoordinate**2)


print(" Theta is :",degrees(Theta)," ","Radius is: ",Radius, ".")