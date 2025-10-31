# basic_version 
#names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#searching_for = "Sam"

#if searching_for in names:
#    print(f"{searching_for} was found in your list.")
#else:
#    print("{searching_for} was not found in the list.")

#advanced_version
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
searching_for = input("Who's name do you want to search for? ")

if searching_for in names:
    print(f"{searching_for} was found in your list.")
else:
    print(f"{searching_for} was not found in your list.")