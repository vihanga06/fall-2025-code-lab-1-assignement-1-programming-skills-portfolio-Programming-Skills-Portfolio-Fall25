#advanced_version
capitals_of_europe = {
    "Germany": "Berlin",
    "Austria": "Vienna",
    "Poland": "Warsaw",
    "France": "Paris",
    "Estonia": "Tallinn",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "Italy": "Rome",
    "UK": "London",
    "Serbia": "Belgrade"
}

print("Countries quiz??")
print("Write the capital of these 10 countries!")

score = 0 

for country, capital in capitals_of_europe.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct\n")
        score += 1
    else:
        print(f"Wrong answer bud. It's {capital}.\n")

print(f"You got {score} out of {len(capitals_of_europe)} correct, nice try")

#added the score thing to make the person know how many mistakes they made.