peserta = int(input("Masukkan jumlah peserta didik: "))
print("Masukkan tinggi masing-masing peserta didik: ")

tinggi = [0 for i in range (peserta)]
for i in range(peserta):
    tinggi[i] = int(input(""))

print("Masukkan gender masing-masing peserta didik :")

gender = ['a' for i in range (peserta)]
for i in range(peserta):
    gender[i] = input("")

tinggiCowo = -1
tinggiCewe = -1
for i in range(peserta):
    if(gender[i]=='L'):
        if(tinggiCowo == -1 or tinggi[i]>tinggi[tinggiCowo]):
            tinggiCowo = i
    else:
        if(tinggiCewe == -1 or tinggi[i]>tinggi[tinggiCewe]):
            tinggiCewe = i

print("Urutan Mahasiswa Tertinggi: " + str(tinggiCowo+1) + " (tinggi " + str(tinggi[tinggiCowo]) +")" )
print("Urutan Mahasiswi Tertinggi: " + str(tinggiCewe+1) + " (tinggi " + str(tinggi[tinggiCewe]) +")" )