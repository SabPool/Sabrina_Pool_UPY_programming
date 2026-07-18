#12 factorial

n=int(input("ingrese un numero: "))
total=1
i=1

while i<=n:
    total = total + i
    i = i+1
print("factorial: ",total)