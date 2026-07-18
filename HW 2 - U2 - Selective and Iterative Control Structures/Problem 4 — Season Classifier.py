while True:
    # INPUT
    mmin = input("Month number = ").strip().lower()
    if mmin == 'exit':
        break    
    # PROCESS
    try:
        month = int(mmin)
    except ValueError:
        print("Enter a number or 'exit'.")
        continue   
    if month < 1 or month > 12:
        s = "Invalid"
    elif month in (12, 1, 2):
        s = "Winter"
    elif month in (3, 4, 5):
        s = "Spring"
    elif month in (6, 7, 8):
        s = "Summer"
    elif month in (9, 10, 11):
        s = "Fall"     
    # OUTPUT
    if s == "Invalid":
        print("Please enter a number between 1 and 12.")
    else:
        print(s)