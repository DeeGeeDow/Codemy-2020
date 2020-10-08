harga = int(input("Harga sebelum diskon : "))
diskon = int(input("Besar diskon : "))
print("Harga setelah diskon adalah " + str("{:.2f}".format((100-diskon)*harga/100)))