total = 0.0

while True:
    # INPUT
    win = input("weight (lbs) = ").strip().lower()
    if win == 'exit':
        break
    din = input("distance (miles) = ")
    # PROCESS
    try:
        w = float(win)
        d = float(din)
    except ValueError:
        print("Enter a decimal")
        continue  
    if w < 0 or d < 0:
        print("Enter a non negative decimal")
        continue    
    if d <= 100:
        if w <= 5:
            cost = 50.00
        else:
            cost = 80.00
    else:
        if w <= 5:
            cost = 120.00
        else:
            cost = 200.00
            
    total += cost
    # OUTPUT
    print(f"Shipping cost: ${cost:.2f} MXN")
print(f"Total: ${total:.2f} MXN")