#basic_version

name = input("What is your name? ")
age = input("How old are you? ")
place = input("Where do you live? ")

biography = {
    "Name": name,
    "Age": age,
    "Place": place
}

print(f"Name: {biography['Name']}\nAge: {biography['Age']}\nPlace: {biography['Place']}")