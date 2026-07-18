#17 triangulo de asteriscos
#necesitamos una variable n, todos los asterisiticos se van a alinear a la izquierda,
#renglon 1=*, renglon 2=**

n = int(input("Ingrese un numero: "))
for renglon in range(1,n+1):
    print("*"*renglon)