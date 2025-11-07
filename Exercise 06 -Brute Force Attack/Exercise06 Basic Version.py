# basic_version

print("This is a 5 number password. Goodluck cracking it!")
password = "12345"

while input("Enter password: ") != password:
    print("Wrong password. Try again.")

print("You wrote the correct password.")