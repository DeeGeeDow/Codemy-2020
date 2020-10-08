a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))

power=1
res=1
for i in range(c):
    power*=b

for i in range(power):
    res*=a

print("Hasil: " + res)