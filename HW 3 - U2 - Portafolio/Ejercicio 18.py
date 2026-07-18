#18 cuadricula de multiplicacion
#lee un #, se imprime una cuadricula #*#, un numero que contenga una fila y una columna
 
n = int(input("ingrese un numero: "))
for r in range(1, n+1):
    l= " "
    for c in range(1,n+1):
        l=l + str(r * c) + "\t"
    print(l)
