N = int(input("Masukkan N: "))
print("Masukkan angka dari kiri ke kanan: ")
masukan = [0 for i in range(105)]

for i in range(N):
    masukan[i] = int(input(""))

for i in range(N-1,-1,-1):
    print(masukan[i])