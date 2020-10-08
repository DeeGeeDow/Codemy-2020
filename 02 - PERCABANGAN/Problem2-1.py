modal = int(input("Masukkan modal awal : "))
hasil = int(input("Masukkan hasil penjualan : "))

if (modal < hasil):
    print("Mahasiswa TPB mendapat keuntungan "+str(hasil-modal))
elif (modal == hasil):
    print("Mahasiswa TPB tidak mendapat keuntungan maupun kerugian")
else:
    print("Mahasiswa TPB mendapat kerugian "+str(modal-hasil))