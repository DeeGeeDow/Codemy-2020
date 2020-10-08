panjang = int(input("Masukkan jumlah huruf pada tulisan: "))
tulisan = input("Masukkan tulisan: ")
banyakHuruf = [0 for i in range (26)]
possible = True
for i in range(panjang):
    banyakHuruf[ord(tulisan[i])-65]+=1

oddCount = 0
for i in range(26):
    if(banyakHuruf[i]%2==1):
        oddCount+=1
    if(oddCount>1):
        possible = False
        break

if(possible):
    text = "dapat"
else:
    text = "tidak dapat"

print("Tulisan tersebut " + text + " disusun menjadi sebuah palindrom.")
