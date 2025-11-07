#advanced_version

print("This is a 5 number password. Goodluck cracking it!")

password = "12345"
attempts = 5

while attempts > 0 and input("Enter password: ") != password:
    attempts -= 1
    print(f"Wrong password. You have {attempts} attempt(s) left.")

if attempts > 0:
    print("Goodjob on crackin it")
else:
    print("Too many tries. You couldn't crack it.")

