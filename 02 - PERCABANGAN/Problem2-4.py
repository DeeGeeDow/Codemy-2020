print("Masukkan beras merk A!")
harga_A = int(input("Harga : "))
satuan_A = int(input("Satuan : "))
print("Masukkan beras merk B!")
harga_B = int(input("Harga : "))
satuan_B = int(input("Satuan : "))
print("Masukkan beras merk C!")
harga_C = int(input("Harga : "))
satuan_C = int(input("Satuan : "))

termurah = "A"

if (harga_A/satuan_A > harga_B/satuan_B):
    termurah = "B"
    if(harga_B/satuan_B > harga_C/satuan_C):
        termurah = "C"
elif(harga_A/satuan_A > harga_C/satuan_C):
    termurah = "C"

print("Beras termurah adalah beras merk " + termurah + ".")