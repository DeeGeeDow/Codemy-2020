print("Masukkan jam sekarang!")
jam = int(input("Jam : "))
menit = int(input("Menit : "))
detik = int(input("Detik : "))
x = int(input("Masukkan X : "))

time = jam*3600 + menit*60 + detik
time+=x

print("Countdown akan berhenti pada jam "+ str(time//3600) + ", menit " + str((time%3600)//60) +", detik " + str(time%60) + "." )
