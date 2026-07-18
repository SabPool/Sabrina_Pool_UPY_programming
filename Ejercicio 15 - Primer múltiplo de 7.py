#15 primer multiplo de 7 entre 1 rango/break y continues/
#ingrese dos numeros, A y B, %7 tambien que A<B

a = int(input("ingrese un numero para empezar el rango: "))
b = int(input("Ingrese un numero para finalizar el rango: "))
for n in range(a,b+1):
    if n %7 == 0:
        print("Primer multiplo de 7: ", n)
        break