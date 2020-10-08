a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))

print("Bilangan sempurna: ")

def divSum(num):
    val = 1
    if(num==1):
        return 0
    else:
        for i in range (2,int(num**0.5)+1):
            if (num%i==0):
                val += i + num//i
        return val

for i in range (a,b+1):
    if(divSum(i)==i):
        print(i)
