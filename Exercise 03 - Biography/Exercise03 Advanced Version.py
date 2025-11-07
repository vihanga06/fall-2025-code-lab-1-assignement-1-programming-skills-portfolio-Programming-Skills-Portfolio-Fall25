#advanced_version
name = input("What is your full name? ")
hometown = input("Where are you from? ")

while True:
    age1 = input("Enter your age: ")
    if age1.isdigit():
        age = int(age1)
        break
    else:
        print("Please write an actual number for your age.")

bio = {
    "Name": name,
    "Age": age,
    "Hometown": hometown
}

print(f"{bio['Name']}\n{bio['Hometown']}\n{bio['Age']}")