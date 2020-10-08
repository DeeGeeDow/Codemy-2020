A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

print("Bilangan prima dari A hingga B:")

for i in range(A,B+1):
    prime = True
    for j in range(2,int(i**0.5+1)):
        if (i%j==0):
            prime = False
            break
    if(prime):
        print(str(i))