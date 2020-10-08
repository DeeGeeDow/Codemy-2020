n = int(input("Masukkan bilangan: "))

res = 0
while(n>0):
    res+=n%10
    n//=10

print("Jumlah semua digitnya adalah "+str(res))