x = int(input("Masukkan nilai x: "))

def f(a):
    return 2*a*a/3 + 5*a + 7

def g(a):
    return a**0.5 + 3/a

print("f(f(g(" + str(x) + "))) = " + str("{:.4f}".format(f(f(g(x))))))
print("f(g(f(" + str(x) + "))) = " + str("{:.4f}".format(f(g(f(x))))))
print("g(f(f(" + str(x) + "))) = " + str("{:.4f}".format(g(f(f(x))))))