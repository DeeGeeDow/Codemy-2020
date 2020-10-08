N = int(input("Masukkan ukuran tegel : "))
diagonal = input("Masukkan motif diagonal : ")
isi = input("Masukkan nilai isi : ")

for i in range(N):
    for j in range(N):
        if(i==j or i+j==N-1):
            print(diagonal,end="")
        else:
            print(isi,end="")
    print("")