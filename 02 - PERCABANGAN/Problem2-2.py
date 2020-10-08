nilai = int(input("Masukkan nilai akhir : "))

if (nilai>=80):
    print(str(nilai) + " mendapat indeks A")
elif (nilai>=73):
    print(str(nilai) + " mendapat indeks AB")
elif (nilai>=65):
    print(str(nilai) + " mendapat indeks B")
elif (nilai>=57):
    print(str(nilai) + " mendapat indeks BC")
elif (nilai>=50):
    print(str(nilai) + " mendapat indeks C")
elif (nilai>=35):
    print(str(nilai) + " mendapat indeks D")
else :
    print(str(nilai) + " mendapat indeks E")