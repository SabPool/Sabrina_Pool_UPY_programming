import datetime

# PROCESS
# Function to determine whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# PROCESS
# Current month in English (lowercase)
current_month = datetime.datetime.now().strftime("%B").lower()

while True:

    # INPUT
    password = input("Enter a password: ")

    # PROCESS
    valid = True

    # Rule 1
    if len(password) < 8:
        print("Your password must be at least 8 characters.")
        valid = False

    # Rule 2
    if not any(c.isupper() for c in password):
        print("Add at least one uppercase letter.")
        valid = False

    # Rule 3
    if not any(c.islower() for c in password):
        print("Add at least one lowercase letter.")
        valid = False

    # Rule 4
    if not any(c.isdigit() for c in password):
        print("Add at least one number.")
        valid = False

    # Rule 5
    special = "!@#$%^&"
    if not any(c in special for c in password):
        print("Add at least one special character (!@#$%^&).")
        valid = False

    # Rule 6
    digit_sum = sum(int(c) for c in password if c.isdigit())

    if digit_sum != 25:
        print("The digits in your password must add up to 25.")
        valid = False

    # Rule 7
    if not is_prime(len(password)):
        print("Your password length must be a prime number.")
        valid = False

    # Rule 8
    if current_month not in password:
        print("Your password must include the current month in lowercase.")
        valid = False

    # OUTPUT
    if valid:
        print("\nPassword accepted! You passed all validation rules.")
        break

    print("\nPlease try again.\n")
