N = int(input("Banyaknya barang : "))
print("Masukkan harga barang: ")
harga = [0 for i in range(105)]

for i in range(N):
    harga[i] = int(input(""))

diskon = int(input("Masukkan diskon : "))
for i in range(N):
    print((100-diskon)*harga[i]//100)