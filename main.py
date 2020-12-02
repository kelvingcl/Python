def triangulo(num):
    for i in range(num):
        print(" " * (num-i-1) + "*" * (2*i+1))
pisos=input("Ingrese el numero de pisos del triangulo: ")

triangulo(int(pisos))