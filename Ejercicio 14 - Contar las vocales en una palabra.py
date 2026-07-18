#14 contar vocales dentro de una palabra

palabra = input("Ingrese una palabra: ")
contar = 0
for i in palabra.lower():
    if i in "aeiou":
        contar = contar +1
print("Contiene tantas vocales: ", contar)