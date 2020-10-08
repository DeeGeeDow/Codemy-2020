a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

def fungsi(a,b,c):
    return 2*a*a*a + 5*b*b - c

print("f(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(fungsi(a,b,c)))