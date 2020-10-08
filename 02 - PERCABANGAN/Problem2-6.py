status = input("Status: ")
und = input("Mengerti investasi: ")
forwhat = input("Investasi buat apa: ")
time = input("Jangka waktu investasi: ")
nilai = input("Nilai investasi -15%, bagaimana: ")

this = 0

if(status == "Menikah"):
    this+=1
if(und == "Tidak"):
    this+=1
if(forwhat == "Menikah"):
    this+=1
if(time == "<5 tahun"):
    this+=1
if(nilai == "Jual"):
    this+=1

that = 5 - this

print("Jenis investasi yang cocok adalah")
print("RD Pasar Uang, Emas, USD")
if(that<=2):
    print("Deposito")
if(that<=3):
    print("RD Pendapatan Tetap, Obligasi")
if(that>=2 and that<=4):
    print("Properti Tanah")
if(that>=2 and that <=5):
    print("RD Saham, RD Campuran, P2P Lending")
if(that>=3 and that<=5):
    print("Saham")