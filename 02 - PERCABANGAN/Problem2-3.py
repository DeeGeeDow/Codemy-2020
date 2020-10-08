a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
c = float(input("Masukkan nilai c : "))

D = b*b - 4*a*c

if(D > 0):
    akar_1 = (-b-D**(0.5))/(2*a)
    akar_2 = (-b+D**(0.5))/(2*a)
    print("Akar-akar dari persamaan kuadrat ada 2, yakni "+ str(akar_1) + " dan " + str(akar_2) + ".")
elif(D==0):
    akar = -b/(2*a)
    print("Akar-akar dari persamaan kuadrat hanya 1, yaitu " + str(akar) + ".")
else:
    print("Akar-akar dari persamaan kuadrat tidak ada.")