qty = int(input("Masukkan jumlah barang yang dibeli: "))

brg = [0 for i in range (4)]

for i in range (qty):
    masukan = input("Masukkan barang ke-" + str(i+1) + ": ")
    if(masukan=="Sabun"):
        brg[0]+=1
    elif (masukan=="Masker"):
        brg[1]+=1
    elif (masukan=="HandSanitizer"):
        brg[2]+=1
    elif (masukan=="FaceShield"):
        brg[3]+=1

def case1(sabun):
    if (sabun>3):
        return False
    else :
        return True

def case2(hs,sabun):
    if((sabun>0 and hs>2) or (sabun==0 and hs>3)):
        return False
    else:
        return True

def case3(masker,fs):
    if((masker>4 and fs==0) or (masker>2 and fs>0)):
        return False
    else:
        return True

def case4(fs,masker):
    if((fs>4 and masker==0) or (fs>2 and masker>0)):
        return False
    else:
        return True

if(case1(brg[0]) and case2(brg[2],brg[0]) and case3(brg[1],brg[3]) and case4(brg[3],brg[1])):
    text = ""
else:
    text = "tidak "

print("Keranjang belanja " + text + "diperbolehkan.")
