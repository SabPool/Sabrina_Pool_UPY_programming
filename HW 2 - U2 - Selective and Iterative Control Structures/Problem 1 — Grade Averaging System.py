#Grade_Averaging_System
def grade_averaging_system():
    grades = []
    #INPUT
    print("Enter your grades, when you finish enter 'done':")
    #PROCESS
    while True:
        gradein = input("- ").strip().lower() 
        if gradein == 'done':
            break
        try:
            grade = float(gradein)
            grades.append(grade)
        except ValueError:
            print("Enter a valid number or 'done'.") 
    if len(grades) == 0:
        print("Enter at least one grade.")
    else:
        total = sum(grades) / len(grades)
        #OUTPUT
        pf = "Passed" if total >= 7.0 else "Failed"
        print(f"Average: {total:.2f} — {pf}")
if __name__ == "__main__":
    grade_averaging_system()