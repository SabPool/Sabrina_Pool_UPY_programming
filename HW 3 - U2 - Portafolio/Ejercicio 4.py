price =150
#children year > 12 = 30%
#studentes 12<years<25=20% (with id)
#adultos 26-64 = no discount
#viejitos 65 o más = 40% discount

age = int(input("Ingresa la edad: "))
id = input("¿Tiene tarjeta? (si/no): ")

if age < 12:
    rate= .30
elif age <=25 and id == "si":
    rate= .20
elif age <= 64:
    rate= 0
else:
    rate= 0.40
n_price = price*(1-rate)
print(f"Price $: {n_price}")
