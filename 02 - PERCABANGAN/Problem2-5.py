A = input("Masukkan pelaku yang ditunjuk A : ")
B = input("Masukkan pelaku yang ditunjuk B : ")
C = input("Masukkan pelaku yang ditunjuk C : ")

pelaku = A
if(A==B):
    if(B==C):
        print("Tidak ada yang berbohong")
    else:
        print("C berbohong")
else:
    if(B==C):
        print("A berbohong")
        pelaku = B
    elif(A==C):
        print("B berbohong")
    else:
        print("Tidak dapat disimpulkan siapa yang berbohong dan siapa yang jujur")

if(A!=B and B!=C and C!=A):
    print("Pelaku tidak dapat ditentukan")
else:
    print("Pelaku yang memakan kue Tuan Wang adalah " + pelaku)
