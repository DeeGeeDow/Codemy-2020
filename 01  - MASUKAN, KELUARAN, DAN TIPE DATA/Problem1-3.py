A = float(input("Masukkan A:"))
B = float(input("Masukkan B:"))
C = float(input("Masukkan C:"))
D = float(input("Masukkan D:"))

root2 = 2**(-1/2)
ry = A - root2*B - root2*D
rx = C + root2*D - root2*B

import math
print("Jarak harta karun: "+str('{:.2f}'.format(math.sqrt(rx*rx + ry*ry))))