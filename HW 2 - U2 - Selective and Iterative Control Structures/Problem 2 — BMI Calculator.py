while True:
    # INPUT
    win = input("weight = ").strip().lower()
    if win == 'exit':
        break  
    hin = input("height = ") 
    # PROCESS
    w = float(win)
    h = float(hin) 
    bmi = w / (h ** 2)
    if bmi < 18.5:
        tb = "Underweight"
    elif bmi <= 24.9:
        tb = "Normal"
    elif bmi <= 29.9:
        tb = "Overweight"
    else:
        tb = "Obese"   
    # OUTPUT
    print(f"BMI: {bmi:.2f} — {tb}")