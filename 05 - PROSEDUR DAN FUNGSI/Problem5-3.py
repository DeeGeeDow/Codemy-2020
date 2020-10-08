A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

print("KPK dari " + str(A) + ", " + str(B) + ", dan " + str(C) + "adalah " + str(lcm(A,lcm(B,C))) + ".")