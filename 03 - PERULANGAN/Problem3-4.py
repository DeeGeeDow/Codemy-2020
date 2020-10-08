N = int(input("Masukkan nilai N: "))

res = 0

uhuy=10
for i in range(4):
    uhuy/=10
    while (res*res<N):
        res+=uhuy
    
    res-=uhuy

print("Nilai akar N adalah: "+ str("{:.3f}".format(res)))