L = int(input("Masukkan L : "))
R = int(input("Masukkan R : "))
X = int(input("Masukkan X : "))

for a in range (L,R+1):
    satisfy = False
    res = 0
    for b in range (a,R+1):
        if(satisfy):
            print( str(a) + " " + str(b))
        else:
            res+=b
            if(res>=X):
                print(str(a) + " " + str(b))
                satisfy = True
