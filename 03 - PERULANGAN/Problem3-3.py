N = int(input("Masukkan N: "))
print("Deret Fibonacci adalah:")

f1 = -1
f2 = 1

for i in range(N):
    if (i!=N-1):
        inp = f1 + f2
        print(str(inp), end=", ")
        f1 = f2
        f2 = inp
    else:
        print(str(f1+f2))