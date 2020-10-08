banyak = int(input("Masukkan banaknya stik Tuan Wang: "))
print("Masukkan panjang stik:")
stik = [0 for i in range(101)]

for i in range(banyak):
    stik[i] = int(input(""))

print("Daftar segitiga yang dapat dibuat: ")
for i in range(banyak):
    for j in range(i+1, banyak):
        for k in range(j+1, banyak):
            if(stik[i]+stik[j]>stik[k] and stik[j]+stik[k]>stik[i] and stik[k]+stik[i]>stik[j]):
                print(str(stik[i]) + " " + str(stik[j]) + " " + str(stik[k]))