num = int(input("Banyaknya nilai: "))
print("Daftar nilai:")

nilai = [0 for i in range(num)]
sama = [0 for i in range(num)]
counter = 0

for i in range(num):
    nilai[i] = int(input(""))
    for j in range(i):
        if(nilai[i]==nilai[j]):
            doubled = False
            for k in range(counter):
                if(nilai[i]==sama[k]):
                    doubled = True
                    break
            if(not doubled):
                sama[counter]=nilai[i]
                counter+=1

print("Daftar nilai yang dicurigai:")
for i in range(counter):
    print(sama[i])