total = 0.0
while True:
    # INPUT
    dato = input("m³ consumed = ").strip().lower() 
    if dato == 'exit':
        break    
    # PROCESS
    m3 = float(dato)
    if m3 < 0:
        print("Must be a non negative decimal.")
        continue    
    if m3 <= 10:
        t = 8.00
    elif m3 <= 20:
        t = 12.00
    else:
        t = 18.00  
    month = m3 * t
    total += month
    # OUTPUT
    print(f"Month charge: ${month:.2f} MXN")
print(f"Total: ${total:.2f} MXN")