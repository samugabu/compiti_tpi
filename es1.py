#from math import pi
import math
#dato il raggio di una sfera calcola il suo volume

#v = (4/3)/math.PI() * r^3
#superficie = 4 * math.pi * math.pow(raggio, 2)

raggio = float(input("Raggio sfera: "))

V = ((4/3)/math.pi)*math.pow(raggio, 3)
s = 4 * math.pi * math.pow(raggio, 2)

print(f"Il volume è: {V}")
print(f"La superficie è: {s}")