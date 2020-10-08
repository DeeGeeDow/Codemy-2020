wang_1 = int(input("Bilangan ke-1 barisan Wangbonacci : "))
wang_6 = int(input("Bilangan ke-6 barisan Wangbonacci : "))

wang_2 = (wang_6 - 3*wang_1)//5

print("Enam bilangan pertama adalah " + str(wang_1) + ", " + str(wang_2) + ", " + str(wang_1 + wang_2) + ", " + str(wang_1 + 2*wang_2) + ", " + str(2*wang_1 + 3*wang_2) + ", " + str(wang_6))