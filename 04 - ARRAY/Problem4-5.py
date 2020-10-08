DNA = input("Masukkan rantai DNA: ")
pola = input("Masukkan pola yang dicari: ")
found = pola in DNA

if(found):
    print("Pola muncul pada rantai DNA")
else:
    print("POla tidak muncul pada rantai DNA")