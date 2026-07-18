#13 suma de numeros pares
#suma numeros pares hasta la numero N
n = int(input("Ingresa un numero: "))
res=0
for i in range(2,n+1,2):
    res = res + i
print("suma de pares:",res)