value = input("Please enter your username:\n")

print(f'Username:{value}')

value1 = input("Please enter your password:\n")
while value1 != "password":
    print("Incorrect password, try again.")
    value1 = input("Please enter your password.\n")

print("Password Confirmed. Signing in...")

